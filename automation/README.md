# AURIX Test Automation

This folder contains automated UI tests created for the AURIX QA Technical Evaluation.

## Tools Used
- Python
- Playwright
- Chromium

## Automated Test Scenarios

### 1. Successful Login
**File:** `test_aurix.py`

Verifies that a registered user can log in using valid credentials and successfully access the authenticated application.

### 2. Invalid Password Login
**File:** `test_invalid-login.py`

Verifies that the application rejects a login attempt when a valid email address is used with an incorrect password.

### 3. Empty Login Fields
**File:** `test_empty_login.py`

Verifies that the application does not allow login when the email and password fields are left empty.

## Security

Login credentials are not stored directly in the automation scripts. Environment variables are used for sensitive authentication data.

## Running the Tests

Install Playwright:

    pip install playwright
    playwright install

Set the required environment variables before running the valid-login test.

Run the tests individually:

    python test_aurix.py
    python test_invalid-login.py
    python test_empty_login.py

## Test Coverage

The automation focuses on critical authentication functionality, including positive and negative login scenarios.
