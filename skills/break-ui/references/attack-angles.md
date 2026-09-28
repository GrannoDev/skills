# Attack angles

Each section is one agent's brief. Paste the section into the agent's prompt. Skip attacks that don't fit the platform.

## Input

Try every text field, number field, picker and upload with:

- Empty, whitespace only, and leading or trailing spaces.
- Very long text (10,000+ characters), and a single very long word with no spaces.
- Emoji, combining characters (zalgo), right-to-left text (Arabic, Hebrew), and mixed scripts.
- Markup and code: `<b>bold</b>`, `<img src=x onerror=alert(1)>`, `{{7*7}}`, `' OR 1=1 --`. Check it shows as plain text and nothing runs.
- Numbers: 0, negative, decimals, very large, `1e308`, leading zeros, and a comma vs a dot as the decimal separator.
- Dates: 29 February, 31st of short months, far past and far future, and the day of a daylight saving change.
- Emails, phones and URLs that are almost valid.
- Pasting instead of typing, and editing the middle of a filled field.
- Uploads: an empty file, a huge file, the wrong type with the right extension, and a filename with spaces and unicode.

Watch for: crashes, text that overflows or gets cut off, input silently changed or dropped, values saved differently from what was shown, and markup that renders or runs.

## Timing and repetition

- Double- and triple-click every submit, save, delete and "next" button.
- Click things while the app is loading or saving.
- Toggle switches, checkboxes and tabs rapidly.
- Submit a form, then immediately navigate away or go back.
- Open and close modals, menus and sheets quickly and repeatedly.
- Interact before the page or screen has finished loading.
- Slow the network if you can (browser throttling, or a slow proxy) and repeat the above.

Watch for: duplicate records or requests, spinners that never stop, buttons that stay disabled, stale data shown after a save, and actions applied to the wrong item.

## Navigation and state

- Use back and forward in the middle of every multi-step flow.
- Reload in the middle of flows, with a modal open, and right after saving.
- Open deep links or URLs straight to later steps, detail pages and settings, both signed in and signed out.
- Open the same item in two tabs or windows, edit it in both, and save both.
- Sign out in one tab and keep using another.
- Let the session expire, or clear cookies and storage, mid-flow.
- On mobile: background the app and bring it back, kill and relaunch it mid-flow, rotate the device, and open a deep link while the app is already open.

Watch for: lost input, wrong screen after returning, steps that can be skipped, protected pages reachable without signing in, one tab overwriting another without warning, and blank or stuck screens.

## Layout and viewport

- Narrow widths (320px), wide (2560px), and very short heights.
- Browser zoom at 50%, 200% and 400% (400% is the WCAG reflow check).
- Long names, titles and numbers everywhere they appear (reuse long values from the Input angle).
- Lists with zero, one and hundreds of items.
- Dark mode, and a right-to-left language if the app supports one.
- Reduced motion turned on (emulate `prefers-reduced-motion` in the browser's dev tools, or the Reduce Motion setting on the device).
- Hardware acceleration disabled in the browser settings, if the tool allows it.
- On mobile: the largest Dynamic Type or font size, landscape, small devices (iPhone SE size), and the on-screen keyboard covering inputs.

Watch for: overlapping or cut-off content, horizontal scrolling, buttons pushed off screen, text unreadable against its background, controls you can't reach, animations that still play with reduced motion on, and effects that stutter or break without hardware acceleration.

## Failure paths

- Go offline mid-action (browser offline mode, airplane mode on the device), then come back online.
- Block or fail API requests if you can (browser request blocking, a proxy), including a slow response that times out.
- Deny permissions: camera, photos, location, notifications, clipboard.
- Visit screens with no data, and a page or item that doesn't exist (bad ID in the URL or deep link).
- Submit data the server should reject, for example a duplicate name or a value above a limit.

Watch for: blank screens, raw error messages or stack traces, errors that don't say what to do, retries that duplicate data, and a UI that says something saved when it didn't.

## Keyboard and accessibility

- Tab through every screen. Check every control is reachable, in a sensible order, with a visible focus ring.
- Open modals and menus with the keyboard. Check Escape closes them and focus goes back to where it was.
- Press Enter in forms and Space on buttons and checkboxes.
- Check for focus traps you can't tab out of, and focus lost to the top of the page after an action.
- Read the accessibility tree, or use a screen reader (VoiceOver on iOS, TalkBack on Android) if the tool allows. Look for buttons and images with no label, and form fields with no name.

Watch for: things only reachable with a mouse or touch, unlabeled controls, focus that jumps or disappears, and keyboard shortcuts that fire while typing in a field.
