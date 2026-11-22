# Interview coding conventions

- Python 3, Flask, pytest, requests.
- Implement only the current interview requirement, without guessing follow-ups.
- Prefer simple, readable functions and minimal dependencies.
- Use Flask's test client for endpoint tests and pytest's tmp_path for file tests.
- Mock external APIs in tests; set explicit timeouts for outbound requests.
- Keep secrets in environment variables; do not log API keys.
- Run tests and report what passed and what failed; don't claim tests ran if they didn't.
- Explain substantive changes concisely.
