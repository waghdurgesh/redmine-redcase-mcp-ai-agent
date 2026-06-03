from mcp.server.fastmcp import FastMCP
from redcase_client import RedcaseClient

mcp = FastMCP("Redcase MCP")


@mcp.tool()
def create_testcases(payload: dict) -> dict:
    """
    Create Redcase testcases in Redmine.
    """

    client = RedcaseClient()

    client.login()

    created = []

    for testcase in payload.get("testcases", []):
        result = client.create_testcase(testcase)
        created.append(result)

    return {
        "success": True,
        "message": "Testcases processed",
        "created": created
    }


if __name__ == "__main__":
    mcp.run()