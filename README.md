# Python API Test Automation

API test automation project built with **Python, pytest, and requests**.

The project demonstrates automated REST API testing using a reusable API client, pytest fixtures, parametrized tests, positive and negative scenarios, and response validation.

## Tech Stack

- Python
- pytest
- requests
- pytest-html
- REST API
- Git / GitHub

## Test Coverage

The automated tests cover:

- GET, POST, and DELETE requests
- HTTP status code validation
- JSON response validation
- Positive and negative test scenarios
- Parametrized test cases
- Response data type and required field validation
- Response time validation
- Content-Type validation

The tests use the JSONPlaceholder REST API as the system under test.

## Project Structure

```text
python-api-automation/
├── config/
│   └── config.py
├── tests/
│   ├── test_posts.py
│   ├── test_users.py
│   └── test_response_quality.py
├── utils/
│   └── api_client.py
├── conftest.py
├── pytest.ini
└── requirements.txt
```

## Setup

Clone the repository:

```bash
git clone https://github.com/tasa1998/python-api-test-automation.git
cd python-api-test-automation
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running Tests

Run all tests:

```bash
pytest -v
```

Run smoke tests:

```bash
pytest -m smoke -v
```

Run negative tests:

```bash
pytest -m negative -v
```

Generate an HTML report:

```bash
pytest --html=report.html --self-contained-html
```

## Framework Design

A reusable `ApiClient` encapsulates HTTP communication and common configuration such as the base URL and request timeout.

Pytest fixtures provide reusable test dependencies and test data, while parametrization allows the same scenario to be executed against multiple data sets without duplicating test code.

## Future Improvements

- JSON Schema validation
- Enhanced logging
- Additional API scenarios
- CI execution with GitHub Actions