# Delivery requirements

Read during exploration so applicable before evidence exists before edits.

## Required evidence

| Work | UI | Non-UI |
| --- | --- | --- |
| Bug fix | Before and after screenshots **and** video recordings of the reproduced flow. | Before and after pseudocode, each linked to the actual implementation file. Include the reproduction and observed result. |
| Feature with an applicable baseline | Before and after screenshots **and** video recordings of the changed flow. | Before and after pseudocode linked to the implementation, plus a runnable demonstration and observed result. |
| Feature without an applicable baseline | Screenshot and video demonstration of the feature. | Pseudocode linked to the implementation, plus a runnable demonstration and observed result. |

For mixed work, provide UI captures and explain changed non-UI behavior with linked pseudocode. A missing baseline is not the same as an inapplicable baseline; disclose missing evidence.

## UI capture

- Capture screenshots at **1920 x 1080** and recordings at **1920 x 1080, 1080p**. Keep the same viewport, input, test data, starting state, and interaction sequence before and after. Show the trigger and outcome; a still-image slideshow is not a recording.
- Use supported browser/device capture tools or the project's existing recording setup. Capture the running implementation, not a mockup. Verify image dimensions and encoded video dimensions from the output files; inspect the screenshots and play the recordings to confirm the intended flow appears.
- For portrait/native targets, preserve their aspect ratio within a 1920 x 1080 recording frame. Identify the target dimensions. Do not stretch or upscale lower-resolution captures and call them 1080p.
- Keep artifacts in a task-specific directory outside the repository unless requested otherwise. Label before, after, or demo explicitly and link playable/viewable files in the final response. Exclude credentials and private user data from the capture.
- If recording, resolution, or playback support is unavailable, report the exact missing evidence. Supply available evidence without representing it as meeting the requirement.

## Non-UI explanation

Use short domain pseudocode that explains behavior, not a transcription of the implementation. For example:

```text
Before: A retry creates another reservation for the same request.
After: A retry returns the reservation stored for that request.
```

Link each explanation to the actual source file and a verified line. For before code whose lines changed, use a resolvable baseline revision/diff link when available, or a clearly labeled read-only source snapshot outside the repository. Never point a before explanation at an after line that now does something different. Include an actual input and independently expected output, then report what happened when run.

## Try-it link

- Prefer the project's existing dev/preview runtime. Start or reuse it through supported tools, then provide a clickable URL to the actual changed flow, with only necessary setup or test-account instructions.
- For non-UI work, use an existing API playground, executable notebook, or supported interactive demo entry point. If needed, add a minimal local demo that calls the real implementation within the approved scope. A source, screenshot, or recording link alone does not satisfy the try-it requirement.
- Open the exact link and perform the intended interaction before handing it over. A responsive root page or successful build alone does not verify the demo. State whether the link is local, requires a runtime to remain running, or has a known expiration. Keep a local runtime alive through the host's managed process tools.
- If the host cannot expose a clickable runnable demo, provide the exact reproduction command and linked example as fallback, mark the try-it requirement blocked, and name the missing capability. Do not invent a URL or imply that opening a source file runs it.
