from unittest.mock import patch

from src.mcp_server import create_testcases


@patch("src.mcp_server.RedcaseClient")
def test_create_testcases(mock_client):

    client_instance = mock_client.return_value

    client_instance.create_testcase.return_value = {
        "success": True,
        "issue_id": "123"
    }

    payload = {
        "testcases": [
            {
                "title": "Login Test",
                "steps": ["step"],
                "expected_results": ["result"]
            }
        ]
    }

    result = create_testcases(payload)

    assert result["success"] is True

    assert len(
        result["created"]
    ) == 1