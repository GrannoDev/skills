# Attack angles

Use applicable rows within the authorized target and budget. Each row can be a delegated brief.

| Angle | Concrete probes | Look for |
| --- | --- | --- |
| Input | Empty/whitespace; 10,000-character text and unbroken words; emoji/combining/RTL; paste/mid-field edits; markup such as `<b>x</b>`, `{{7*7}}`, harmless injection markers; 0/negative/decimal/huge numbers, comma/dot separators; leap days/DST; almost-valid contacts/URLs; empty/huge/wrong-type uploads with Unicode filenames | Crashes, overflow, silently changed values, displayed/saved mismatch, interpreted markup/code |
| Timing and repetition | Double/triple submit/save/delete; interact during loading/saving; rapid toggles and modal cycles; submit then navigate/back; repeat with slow network | Duplicate effects, permanent spinners/disabled buttons, stale or wrong-item updates |
| Navigation and state | Back/forward/reload mid-flow; deep links signed in/out; concurrent edits in two tabs; sign out/expire one session; mobile background/relaunch/rotation/deep links | Lost input, skipped steps, unauthorized access, silent overwrites, stuck screens |
| Layout and viewport | 320px/2560px widths, short heights, 50%/200%/400% zoom; zero/one/hundreds of records; long labels; supported dark/RTL modes; reduced motion; optional hardware-acceleration fallback; mobile large fonts/landscape/keyboard | Clipping, overlap, unreachable controls, unreadable contrast, overflow, ignored motion preference, rendering failures |
| Failure paths | Offline/reconnect mid-action; blocked requests/timeouts; denied device permissions; absent records/bad IDs; server-rejected duplicates/limits | Blank screens, leaked internals, unclear errors, duplicate retries, false save success |
| Keyboard and accessibility | Tab order/focus; keyboard-open menus/modals; Escape and focus return; Enter/Space; focus traps/loss; accessible names; screen reader when available | Mouse-only actions, missing labels, vanished focus, shortcuts firing while typing |
