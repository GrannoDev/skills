# Lenses

Each section is one way to look at a feature. Turn every bullet that fits into a concrete "What if…?" about this feature, using its real inputs, fields and screens. Skip bullets that don't fit.

## Boundaries

- Zero, one, and many.
- The maximum, one over the maximum, and one under the minimum.
- Empty collections, empty strings, and a single item.
- Negative numbers where only positives make sense.
- Inclusive vs exclusive range ends: is the last day, the limit, or the cutoff itself allowed?
- Pagination: exactly one full page, one item over, and the last page.

## Data shape

- A field that's missing, null, or undefined.
- The wrong type: a string where a number is expected, an object where a list is expected.
- Whitespace only, and leading or trailing spaces.
- Emoji, combining characters, right-to-left text, and mixed scripts.
- Very long values, and a single very long word.
- Duplicates, and the same value with different casing.
- Items in an unexpected order.
- Extra fields the code doesn't know about.

## Time

- Timezones: the user, the server and the database in different zones.
- Daylight saving changes: the missing hour and the repeated hour.
- 29 February, month ends, and year ends.
- Midnight, and the exact instant something expires or starts.
- A clock that's wrong or skewed between machines.
- Something that starts before and finishes after a deadline.

## State and lifecycle

- The very first run, with no data at all.
- Data left half-written by an earlier failure.
- Doing the same thing twice: is it idempotent?
- Retrying after a partial failure.
- Records created before a migration or an older version of the feature.
- An entity deleted, archived or changed while the feature is using it.
- Undo, cancel, or going back halfway through.

## Concurrency

- The same request submitted twice in quick succession.
- Two users changing the same record.
- Reading data that changed since it was loaded.
- Events or messages arriving out of order, twice, or not at all.
- A background job running while the user edits the same data.

## Dependency failure

- A dependency that times out, is slow, or is down.
- An error response (4xx, 5xx) or a malformed response.
- Rate limits and quota errors.
- Disk full, or a file missing or locked.
- A dependency that succeeds but returns empty or partial data.
- A failure after some side effects already happened (email sent, card charged).

## Auth and security

- Not logged in, or the session expires mid-flow.
- Another user's or tenant's ID in the request.
- A role or permission that changes while the user is in the flow.
- User input that ends up in SQL, HTML, shell commands, file paths or templates.
- Secrets or personal data that could leak into logs, errors or URLs.

## Scale

- 10,000 items instead of 10.
- A very large file or payload.
- A request that gets slow enough to hit a timeout.
- Many users hitting the feature at once.

## Money and numbers

- Rounding: when it happens, and which way.
- Floating-point sums that don't add up (0.1 + 0.2).
- Currencies with zero or three decimal places.
- Discounts, refunds or credits that push a total below zero.
- Locale formats: a comma vs a dot as the decimal separator.

## Environment and configuration

- A feature flag on, off, or changing mid-session.
- A missing or invalid config value.
- Different locales, languages and number formats.
- An old client talking to a new server, or the other way round.
