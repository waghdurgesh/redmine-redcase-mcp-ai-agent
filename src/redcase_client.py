import os
import json
import re

from pathlib import Path
from typing import Dict, List

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("REDMINE_USERNAME")
PASSWORD = os.getenv("REDMINE_PASSWORD")

if not USERNAME or not PASSWORD:
    raise ValueError(
        "REDMINE_USERNAME and REDMINE_PASSWORD must be configured"
    )


def load_config() -> Dict:

    config_path = (
        Path(__file__).parent.parent
        / "config"
        / "redcase_config.json"
    )

    if not config_path.exists():
        raise FileNotFoundError(
            "config/redcase_config.json not found"
        )

    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)


CONFIG = load_config()

VERIFY_CERT_PATH = CONFIG["ssl_cerificate"]

BASE_URL = CONFIG["base_url"]
PROJECT_SLUG = CONFIG["project_slug"]

FORM_UPDATE_TRIGGERED_BY = CONFIG["form_update_triggered_by"]

IS_PRIVATE = CONFIG["is_private"]

AUTHOR_ID = CONFIG["author_id"]
TRACKER_ID = CONFIG["tracker_id"]

STATUS_ID = CONFIG["status_id"]
PRIORITY_ID = CONFIG["priority_id"]

ASSIGNED_TO_ID = CONFIG["assigned_to_id"]
FIXED_VERSION_ID = CONFIG["fixed_version_id"]
PARENT_ISSUE_ID = CONFIG["parent_issue_id"]

TEST_SUITE_ID = CONFIG["test_suite_id"]

START_DATE = CONFIG["start_date"]
DUE_DATE = CONFIG["due_date"]

ESTIMATED_HOURS = CONFIG["estimated_hours"]

DONE_RATIO = CONFIG["done_ratio"]

SUBJECT = CONFIG["subject"]
DESCRIPTION = CONFIG["description"]

WATCHER_USER_IDS = CONFIG.get(
    "watcher_user_ids",
    []
)

WAS_DEFAULT_STATUS = CONFIG["was_default_status"]

COMMIT = CONFIG["commit"]

LOGIN_URL = f"{BASE_URL}/login"

NEW_ISSUE_URL = (
    f"{BASE_URL}/projects/{PROJECT_SLUG}/issues/new"
)

CREATE_ISSUE_URL = (
    f"{BASE_URL}/projects/{PROJECT_SLUG}/issues"
)


def sanitize_text(text: str) -> str:

    if not text:
        return ""

    text = re.sub(
        r"<script.*?>.*?</script>",
        "",
        text,
        flags=re.I | re.S
    )

    return text.strip()


def list_to_html(items: List[str]) -> str:

    if not items:
        return ""

    html = ""

    for index, item in enumerate(items, start=1):
        html += (
            f"<p>{index}. "
            f"{sanitize_text(item)}</p>\n"
        )

    return html


class RedcaseClient:

    def __init__(self):

        self.session = requests.Session()

        self.session.headers.update({
            "User-Agent": "Mozilla/5.0"
        })

    def login(self):

        login_page = self.session.get(
            LOGIN_URL,
            verify=VERIFY_CERT_PATH
        )

        soup = BeautifulSoup(
            login_page.text,
            "html.parser"
        )

        token_input = soup.find(
            "input",
            {"name": "authenticity_token"}
        )

        if not token_input:
            raise Exception(
                "Unable to find authenticity token"
            )

        csrf_token = token_input["value"]

        payload = {
            "username": USERNAME,
            "password": PASSWORD,
            "authenticity_token": csrf_token,
            "login": "Login"
        }

        response = self.session.post(
            LOGIN_URL,
            verify=VERIFY_CERT_PATH,
            data=payload,
            allow_redirects=True
        )

        if "/login" in response.url:
            raise Exception("Login failed")

        print("Login successful")

    def get_issue_csrf_token(self):

        response = self.session.get(
            NEW_ISSUE_URL,
            verify=VERIFY_CERT_PATH
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        token = soup.find(
            "input",
            {"name": "authenticity_token"}
        )

        if not token:
            raise Exception(
                "Unable to fetch issue token"
            )

        return token["value"]

    def build_payload(
        self,
        testcase: Dict,
        csrf_token: str
    ):

        return {

            "authenticity_token":
                csrf_token,

            "form_update_triggered_by":
                str(FORM_UPDATE_TRIGGERED_BY),

            "issue[is_private]":
                str(IS_PRIVATE),

            "issue[author_id]":
                str(AUTHOR_ID),

            "issue[tracker_id]":
                str(TRACKER_ID),

            "issue[subject]":
                testcase.get(
                    "title",
                    SUBJECT
                ),

            "issue[description]":
                testcase.get(
                    "description",
                    DESCRIPTION
                ),

            "issue[status_id]":
                str(STATUS_ID),

            "was_default_status":
                str(WAS_DEFAULT_STATUS),

            "issue[priority_id]":
                str(
                    testcase.get(
                        "priority_id",
                        PRIORITY_ID
                    )
                ),

            "issue[assigned_to_id]":
                str(ASSIGNED_TO_ID),

            "issue[fixed_version_id]":
                str(FIXED_VERSION_ID),

            "issue[parent_issue_id]":
                str(PARENT_ISSUE_ID),

            "issue[start_date]":
                testcase.get(
                    "start_date",
                    START_DATE
                ),

            "issue[due_date]":
                testcase.get(
                    "due_date",
                    DUE_DATE
                ),

            "issue[estimated_hours]":
                str(ESTIMATED_HOURS),

            "issue[done_ratio]":
                str(DONE_RATIO),

            "issue[test_case_attributes][test_suite_id]":
                str(TEST_SUITE_ID),

            "issue[test_case_attributes][preconditions]":
                list_to_html(
                    testcase.get(
                        "preconditions",
                        []
                    )
                ),

            "issue[test_case_attributes][steps]":
                list_to_html(
                    testcase.get(
                        "steps",
                        []
                    )
                ),

            "issue[test_case_attributes][expected_results]":
                list_to_html(
                    testcase.get(
                        "expected_results",
                        []
                    )
                ),

            "issue[watcher_user_ids][]":
                WATCHER_USER_IDS,

            "commit":
                str(COMMIT)
        }

    def create_testcase(
        self,
        testcase: Dict
    ) -> Dict:

        if not testcase.get("title"):
            return {
                "success": False,
                "error": "Missing title"
            }

        csrf_token = (
            self.get_issue_csrf_token()
        )

        payload = self.build_payload(
            testcase,
            csrf_token
        )

        response = self.session.post(
            CREATE_ISSUE_URL,
            verify=VERIFY_CERT_PATH,
            data=payload,
            allow_redirects=True
        )

        issue_match = re.search(
            r"/issues/(\\d+)",
            response.url
        )

        issue_id = (
            issue_match.group(1)
            if issue_match
            else None
        )

        return {
            "success": True,
            "issue_id": issue_id,
            "title": testcase["title"],
            "url": response.url
        }