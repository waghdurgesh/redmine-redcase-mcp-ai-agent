from src.redcase_client import RedcaseClient


def test_build_payload():

    client = RedcaseClient()

    testcase = {
        "title": "Login Validation",
        "description": "Verify login",

        "preconditions": [
            "User exists"
        ],

        "steps": [
            "Open login page",
            "Login"
        ],

        "expected_results": [
            "Dashboard displayed"
        ]
    }

    payload = client.build_payload(
        testcase,
        "fake-token"
    )

    assert (
        payload["authenticity_token"]
        == "fake-token"
    )

    assert (
        payload["issue[subject]"]
        == "Login Validation"
    )

    assert (
        payload["issue[description]"]
        == "Verify login"
    )

    assert (
        payload[
            "issue[test_case_attributes][steps]"
        ]
        != ""
    )