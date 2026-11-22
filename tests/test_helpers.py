import json
from unittest.mock import Mock, patch

from helpers import post_json, read_csv_rows, write_json


def test_csv_json_roundtrip(tmp_path):
    csv_path = tmp_path / "input.csv"
    csv_path.write_text("id,text\n1,refund request\n", encoding="utf-8")

    rows = read_csv_rows(csv_path)
    assert rows == [{"id": "1", "text": "refund request"}]

    json_path = tmp_path / "output.json"
    write_json(json_path, rows)
    assert json.loads(json_path.read_text(encoding="utf-8")) == rows


def test_post_json_mocks_network_call():
    response = Mock()
    response.json.return_value = {"category": "billing"}

    with patch("helpers.requests.post", return_value=response) as post:
        result = post_json("https://example.invalid/generate", {"text": "refund"})

    assert result == {"category": "billing"}
    post.assert_called_once_with(
        "https://example.invalid/generate",
        json={"text": "refund"},
        timeout=10,
    )
    response.raise_for_status.assert_called_once_with()
