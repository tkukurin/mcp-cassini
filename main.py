# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "fastmcp>=4.0.5",
# ]
# ///
port = 8090

import os

from fastmcp import FastMCP
from fastmcp.server.auth.providers.jwt import StaticTokenVerifier

mcp = FastMCP(
    "Pebble demo",
    auth=StaticTokenVerifier(
        tokens={
            os.environ["MCP_TOKEN"]: {"client_id": "pebble", "scopes": []}
        }
    ),
)


@mcp.tool
def hello(name: str) -> str:
    """Greet someone by name. Use this to test the Pebble integration."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    mcp.run(
        transport="http",
        host="127.0.0.1",
        port=port,
        stateless_http=True,
        json_response=True,
    )
