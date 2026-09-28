# Checklist

Concrete things worth checking on almost every feature. Not every item applies to every feature, so skip the ones that don't fit. Use the Frontend list when the feature has a UI, the Backend list when it runs on a server, and both when it does both. For anything else, such as a library or a CLI, take the items from either list that fit.

Turn each item that fits into a "What if…?" about this feature, using its real screens, fields and endpoints.

## Frontend

### Network

- The user has a poor connection. Throttle it (Slow 3G or Slow 4G in the browser's dev tools) and use the feature.
- The user loses connection while using the feature, then gets it back.
- The request returns an error: 4xx, 5xx, or a timeout.
- The request returns null, an empty list, or an empty object.
- The request takes much longer than usual, or two responses arrive in the wrong order (a search box that fires on every keystroke).
- The session expires and the request comes back as 401.

### Input

- The text value has an extremely large number of characters: 10,000+, and a single long word with no spaces.
- The text value has no characters, almost none (one character), only whitespace, or leading or trailing spaces.
- The text value contains emoji, combining characters, right-to-left text, mixed scripts, or line breaks pasted in from somewhere else.
- A list shows zero items, one item, or 10,000 items.

### Interaction

- The user spam-clicks the element.
- The user navigates away, reloads, or presses back in the middle of an action.
- The user has the same page open in two tabs and changes it in both.

### Accessibility and display

- The user has reduced motion turned on (`prefers-reduced-motion`).
- The user's browser has hardware acceleration disabled. Watch animations, blur and `backdrop-filter`, canvas and video.
- The user is browsing zoomed in or out. Check from 50% up to 200%, and 400% for the WCAG reflow check.
- The user can't use a mouse or pointer and navigates by keyboard only.
- The user relies on a screen reader. Check labels, and that loading, errors and success are announced.
- The user has a larger default font size in the browser settings (this is different from zoom).
- The user is on a narrow screen (320px) or a touch device.
- The user has dark mode or forced colors (Windows high contrast) turned on.
- The text is translated into a longer language, such as German.

## Backend

### Requests

- The request body is empty, missing a field, has a field of the wrong type, or has fields the code doesn't know about.
- The request body or an uploaded file is extremely large.
- The same request arrives twice (a retry or a double submit). Is it idempotent?
- The caller isn't authenticated, or sends another user's or tenant's ID.
- An old client calls the new version of the endpoint, or the other way round.

### Dependencies

- A downstream call (database, another service, a third-party API) returns an error, times out, is down, or returns a malformed response.
- A downstream call returns null, empty, or partial data.
- A downstream call is rate limited.
- The operation fails halfway, after some side effects already happened (a row written, an email sent, a card charged).

### Data and load

- Two requests change the same record at the same time.
- A query returns 10,000+ rows instead of 10. Watch for missing pagination, N+1 queries and missing indexes.
- Many users hit the endpoint at once.
- The server, the database and the user are in different timezones.

### Errors and logs

- An error response leaks a stack trace, SQL, or internal IDs to the caller.
- Personal data or secrets end up in the logs, error messages or URLs.
