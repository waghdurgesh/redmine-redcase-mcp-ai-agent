from src.redcase_client import RedcaseClient


def test_missing_title():

    client = RedcaseClient()

    result = client.create_testcase(
        {
            "steps": ["step"],
            "expected_results": ["result"]
        }
    )

    assert result["success"] is False


def test_missing_steps():

    client = RedcaseClient()

    result = client.create_testcase(
        {
            "title": "Test"
        }
    )

    assert result["success"] is False


def test_missing_expected_results():

    client = RedcaseClient()

    result = client.create_testcase(
        {
            "title": "Test",
            "steps": ["step"]
        }
    )

    assert result["success"] is False