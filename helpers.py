"""Optional reference snippets for CSV, JSON and outbound HTTP calls."""

import csv
import json
from pathlib import Path

import requests


def read_csv_rows(path: str | Path) -> list[dict[str, str]]:
    with open(path, newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def write_json(path: str | Path, value: object) -> None:
    with open(path, "w", encoding="utf-8") as file:
        json.dump(value, file, indent=2)


def post_json(url: str, payload: dict, *, timeout: float = 10) -> dict:
    """Example integration; do not call an external service from unit tests."""
    response = requests.post(url, json=payload, timeout=timeout)
    response.raise_for_status()
    return response.json()
