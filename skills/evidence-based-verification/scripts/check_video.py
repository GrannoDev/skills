#!/usr/bin/env python3
"""Check saved video metadata and decoding; visual inspection is still required."""

import argparse
from fractions import Fraction
import json
import math
from pathlib import Path
import shutil
import subprocess
import sys


def positive_number(value):
    number = float(value)
    if not math.isfinite(number) or number <= 0:
        raise argparse.ArgumentTypeError("must be a finite positive number")
    return number


def number(value):
    try:
        result = float(Fraction(str(value)))
        return result if math.isfinite(result) else 0.0
    except (ValueError, ZeroDivisionError):
        return 0.0


def run(command):
    return subprocess.run(command, capture_output=True, text=True, timeout=60)


def inspect_video(path, thresholds):
    report = {
        "file": str(path),
        "thresholds": thresholds,
        "status": "unverified",
        "issues": [],
        "scope": "Metadata and decoding only. Inspect readability and behavior separately.",
    }
    if not path.is_file() or path.stat().st_size == 0:
        report["status"] = "fail"
        report["issues"].append("Video file is missing or empty.")
        return report, 2

    missing = [tool for tool in ("ffprobe", "ffmpeg") if not shutil.which(tool)]
    if missing:
        report["issues"].append("Required tools unavailable: " + ", ".join(missing))
        return report, 3

    probe = run([
        "ffprobe", "-v", "error", "-select_streams", "v:0",
        "-show_entries",
        "stream=width,height,avg_frame_rate,duration,codec_name,pix_fmt:format=duration,size",
        "-of", "json", str(path),
    ])
    if probe.returncode:
        report["status"] = "fail"
        report["issues"].append("ffprobe could not read the video: " + probe.stderr.strip())
        return report, 2

    metadata = json.loads(probe.stdout)
    streams = metadata.get("streams", [])
    if not streams:
        report["status"] = "fail"
        report["issues"].append("No video stream found.")
        return report, 2

    stream = streams[0]
    width, height = int(stream.get("width", 0)), int(stream.get("height", 0))
    fps = number(stream.get("avg_frame_rate"))
    duration = (
        number(stream.get("duration"))
        or number(metadata.get("format", {}).get("duration"))
    )
    report["metadata"] = {
        "width": width, "height": height, "fps": round(fps, 3),
        "duration_seconds": round(duration, 3), "size_bytes": path.stat().st_size,
        "codec": stream.get("codec_name"), "pixel_format": stream.get("pix_fmt"),
    }
    if (
        max(width, height) < thresholds["min_long_edge"]
        or min(width, height) < thresholds["min_short_edge"]
    ):
        report["issues"].append(f"Resolution {width}x{height} is below the configured floor.")
    if fps < thresholds["min_fps"] * 0.995:
        report["issues"].append(f"Declared average frame rate {fps:.3f} is below the configured floor.")
    if duration <= 0:
        report["issues"].append("Video has no positive, measurable duration.")

    decoded = run([
        "ffmpeg", "-nostdin", "-v", "error", "-xerror", "-i", str(path),
        "-map", "0:v:0", "-an", "-f", "null", "-",
    ])
    report["decode"] = (
        "pass" if decoded.returncode == 0 and not decoded.stderr.strip() else "fail"
    )
    if report["decode"] == "fail":
        report["issues"].append(
            "Video decode failed: "
            + (decoded.stderr.strip() or f"exit {decoded.returncode}")
        )

    report["status"] = "fail" if report["issues"] else "pass"
    return report, 2 if report["issues"] else 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("video", type=Path)
    parser.add_argument("--min-long-edge", type=positive_number, default=1280)
    parser.add_argument("--min-short-edge", type=positive_number, default=720)
    parser.add_argument("--min-fps", type=positive_number, default=30)
    args = parser.parse_args()
    thresholds = {
        "min_long_edge": args.min_long_edge,
        "min_short_edge": args.min_short_edge,
        "min_fps": args.min_fps,
    }
    path = args.video.expanduser().resolve()
    try:
        report, code = inspect_video(path, thresholds)
    except (OSError, subprocess.TimeoutExpired, ValueError) as error:
        report = {
            "file": str(path), "thresholds": thresholds,
            "status": "unverified", "issues": [str(error)],
        }
        code = 3
    print(json.dumps(report, indent=2))
    return code


if __name__ == "__main__":
    sys.exit(main())
