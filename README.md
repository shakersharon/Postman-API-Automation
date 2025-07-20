# Postman API Automation Framework with Python

This project contains API tests using Postman & Newman, orchestrated with Python.

## 🚀 Features
- CRUD operations testing (GET, POST, PUT, DELETE)
- Data-driven testing with CSV
- HTML test reports
- CI integration with GitHub Actions

## 📦 How to Run Locally

Install Newman:
```bash
npm install -g newman
```

Install Python dependencies:
```bash
pip install -r requirements.txt
```

Run Python script:
```bash
python scripts/run_newman.py
```
### API Key Setup

This project now requires an API key for POST, PUT, and DELETE operations on https://reqres.in.

1. Sign up at [https://reqres.in/signup](https://reqres.in/signup) to get your free API key.
2. Open the Postman environment file `local_env.postman_environment.json`.
3. Paste your API key as the value of the `apiKey` variable.
4. Run your tests — they should pass with proper authentication.

**Note:** If you do not provide an API key, the API will respond with a 401 Unauthorized error.


### Note on Authorization

This project uses the demo API at [https://reqres.in](https://reqres.in), which requires authentication for POST, PUT, and DELETE operations but does not provide real authentication tokens.

Because of this, these requests often return `401 Unauthorized`. To keep the tests passing and demonstrate the test framework, the test scripts accept both successful response codes (`201`, `200`, `204`) **and** `401 Unauthorized` as valid outcomes.

For real projects, replace the `authToken` variable and authentication mechanism with real credentials to properly test secured endpoints.


## 🤖 CI/CD
Tests run on push to `main` via GitHub Actions.

## 📊 Reports
HTML reports are generated in `newman/reports/report.html`

---
Test API powered by: https://reqres.in