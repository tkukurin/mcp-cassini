# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "fastmcp>=4.0.5",
# ]
# ///

import os
host = "127.0.0.1"
port = os.environ.get("repebble_mcp_port", 8090)

from fastmcp import FastMCP
from fastmcp.server.auth.providers.jwt import StaticTokenVerifier

mcp = FastMCP(
    "Pebble demo",
    auth=StaticTokenVerifier(
        tokens={
            os.environ["repebble_mcp_token"]: {"client_id": "pebble", "scopes": []}
        }
    ),
)


@mcp.tool
def hello(name: str) -> str:
    """Greet someone by name. Use this to test the Pebble integration."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(f'{host}:{port}')
    mcp.run(
        transport="http",
        host=host,
        port=port,
        stateless_http=True,
        json_response=True,
    )
