
# Repebble demo: basic MCP

For **Pebble / Index 01’s MCP Sandbox**, use a standard **Streamable HTTP** MCP server. Pebble accepts bearer-token authentication; OAuth login flows are currently unsupported. ([Pebble Help Center][1])

```fish
# export MCP_TOKEN="$(uv run python -c 'import secrets; print(secrets.token_urlsafe(32))')"
set -gx MCP_TOKEN 'xyz'
printf 'Authorization: Bearer %s\n' "$MCP_TOKEN"
uv run main.py
```

In separate terminal:

```bash
# brew install cloudflared 
cloudflared tunnel --url http://127.0.0.1:8000
# copy temp url eg. url=`https://robin-prizes-hawaiian-balance.trycloudflare.com`
```

Append `$url/mcp`. 
JSON responses because Cloudflare’s temporary tunnels do not support SSE streaming. ([Cloudflare Docs][3])

In Pebble, **MCP & Tool Settings**, create a sandbox group using **Default**, not **Index Agent**. Under **MCP Servers**, add: ([Pebble Help Center][1])
* URL: `$url/mcp`
* transport: streamable HTTP
* auth: `Bearer $MCP_TOKEN`
* setup group `$g`

Assign `$g` to **Double click and hold** in the Index settings.
Double-click and hold, then say: **“Use hello to greet Toni.”**
Custom MCP uses Pebble’s cloud agent, not the offline agent. 
([Pebble Help Center][1])

Replace `hello()` with your actual operation. This is a development setup: the temporary tunnel and `StaticTokenVerifier` are not intended for production deployment. ([Cloudflare Docs][3])

[1]: https://help.repebble.com/en/articles/15724406-index-advanced-features-mcp-webhook "Pebble Index 01 Advanced Features: MCP & Webhooks | Pebble Help Center"
[2]: https://gofastmcp.com/v3/deployment/running-server "Running Your Server - FastMCP"
[3]: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/do-more-with-tunnels/trycloudflare/?utm_source=chatgpt.com "Quick Tunnels · Cloudflare One docs"
