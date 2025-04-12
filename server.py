# server.py
from dotenv import load_dotenv
import os
import logging

# ログ設定
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# .envファイルを読み込む
load_dotenv()

from mcp.server.fastmcp import FastMCP

# Create an MCP server
logger.info("Creating MCP server...")
mcp = FastMCP("Demo")
logger.info("MCP server created")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"


@mcp.resource("file://readme.md")
def readme() -> str:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    readme_path = os.path.join(current_dir, "README.md")

    if not os.path.exists(readme_path):
        raise FileNotFoundError(f"README.md not found in {current_dir}")

    with open(readme_path, "r") as f:
        return f.read()


if __name__ == "__main__":
    logger.info("Starting MCP server...")
    mcp.run()
    logger.info("MCP server started")
