from src.redcase_client import sanitize_text, list_to_html


def test_sanitize_text_removes_script():

    text = "<script>alert('x')</script>Hello"

    result = sanitize_text(text)

    assert result == "Hello"


def test_sanitize_text_empty():

    assert sanitize_text("") == ""


def test_list_to_html():

    result = list_to_html(
        [
            "Step 1",
            "Step 2"
        ]
    )

    expected = (
        "<p>1. Step 1</p>\n"
        "<p>2. Step 2</p>\n"
    )

    assert result == expected


def test_list_to_html_empty():

    assert list_to_html([]) == ""