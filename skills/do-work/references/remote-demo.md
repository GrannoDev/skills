# Remote demo

Read when the runtime runs on a different machine from the user. Include the chosen route in the plan's delivery field. Prefer an existing reachable demo route, then Tailscale when the user has tailnet access, otherwise a Cloudflare Tunnel. Keep the app listening on loopback when proxying it. Commands below assume port 3000; use the actual port.

## Tailscale

Check that the box is connected and the user can access its tailnet. Inspect existing Serve routes before adding one. For an unused endpoint:

```sh
tailscale serve status
tailscale serve --bg http://127.0.0.1:3000
```

Use the HTTPS URL reported by Serve and append the feature's route. If its endpoint is occupied, choose an unused HTTPS port supported by the installed CLI. Preserve existing routes; do not reset Serve. State that the user needs Tailscale access. If login or HTTPS enablement needs human action, report that prerequisite or use Cloudflare when suitable.

See [Tailscale Serve commands](https://tailscale.com/docs/reference/tailscale-cli/serve).

## Cloudflare Tunnel

Reuse an appropriate configured tunnel when available. For a temporary demo with disposable data:

```sh
cloudflared tunnel --url http://127.0.0.1:3000
```

Run it in a managed persistent session. Use the generated HTTPS URL from its output and append the feature's route. A Quick Tunnel is public and lasts while its process runs. Use an authenticated configured tunnel or Tailscale for private data. Preserve existing tunnel configuration. Quick Tunnels do not support server-sent events; use another route if the demo depends on them.

See [Cloudflare Quick Tunnels](https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/).

## Verify and hand over

Open the exact demo URL from a user-side browser or another client with equivalent network/access conditions. Exercise the feature, including assets, API calls, redirects, and WebSockets or streaming when used. Fix hardcoded localhost URLs, host allowlists, or proxy/origin settings only as needed for this demo. A request made solely on the remote box does not establish user-side reachability; disclose when that check is unavailable.

Keep the app and tunnel alive. Deliver viewable capture links through supported artifacts or a route serving only this task's captures, never the repository or a broad filesystem directory. State access requirements and lifetime. Track the task's process/route so later cleanup removes only what this task created, after the user finishes trying it.
