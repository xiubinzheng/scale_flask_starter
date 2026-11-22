# Scale AI Flask backup starter

This is a **minimal Flask backup** in case you choose Flask for a live backend coding exercise. It is **not** a prewritten solution to the CSV/LLM interview problem.

## Requirements

- Python 3.10+
- Internet access for the initial `pip install`

## 1. One-time setup (macOS or Ubuntu)

```bash
cd scale_flask_starter
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## 2. Prove the required test setup works

```bash
python -m pytest -v
```

The tests include the required `assert 1 == 1`, `/hello_world` checking, basic POST validation, CSV/JSON file operations, and a mocked outbound HTTP request.

## 3. Start the server

```bash
python -m flask --app app run --port 8000 --debug
```

Or use `python app.py`. Start only one server on port 8000 at a time (stop your FastAPI server if it is already running there).

## 4. Curl the required endpoint (in another terminal)

```bash
curl -i http://127.0.0.1:8000/hello_world
```

Expected status: **HTTP 200**

Expected body:

```json
{"hello":"world"}
```

Optional POST example:

```bash
curl -i -X POST http://127.0.0.1:8000/echo \
  -H 'Content-Type: application/json' \
  -d '{"text":"hello"}'
```

## What's in the files?

- `app.py`: Flask app and GET `/hello_world`, POST `/echo` examples.
- `tests/test_app.py`: Flask test-client examples and the required trivial assertion.
- `helpers.py`: small helpers for reading CSV, writing JSON and making outbound HTTP POST requests.
- `tests/test_helpers.py`: CSV/JSON temp-file test and a mocked HTTP call.
- `data/sample.csv`: sample practice data.
- `CLAUDE.md`: short development conventions only (no interview solution).

## During the interview

1. Start from this working baseline and follow the interviewer's requirements.
2. For CSV/JSON tasks, use the `helpers.py` patterns, but adapt to the actual input and output contract.
3. For model APIs, take the provided API URL and key from the interviewer. Keep the key in an environment variable.
4. Add one endpoint and one test at a time.
5. Demonstrate the result with curl and pytest.

**Safety note:** File paths supplied by an HTTP client are untrusted. For a real deployed service, limit reads and writes to an approved directory, and consider size limits. For the local interview exercise, follow the explicit specification.
