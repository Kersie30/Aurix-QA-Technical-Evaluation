# AURIX API Testing

This folder contains the Postman API collection used during the AURIX QA Technical Evaluation.

## Tool Used

- Postman

## Collection File

`AURIX COLLECTION.postman_collection.json`

## API Areas Covered

### Authentication

The collection includes requests for:

- GET Login Page
- POST Valid Login
- GET Current User
- GET Unauthorized Current User
- POST Wrong Password

### Wallet Operations

The collection includes:

- POST Buy - Valid Transaction
- POST Sell - Valid Transaction

### Transactions

The collection includes:

- GET Transaction History

## Test Objectives

The API testing focused on:

- Valid authentication
- Invalid authentication
- Unauthorized access
- Current user/session validation
- Wallet buy operations
- Wallet sell operations
- Transaction history retrieval
- Response status and behaviour

## How to Use the Collection

1. Open Postman.
2. Click **Import**.
3. Select `AURIX COLLECTION.postman_collection.json`.
4. Import the collection.
5. Review the required request parameters before running the requests.
6. Execute the requests individually in the order shown in the collection.

## Security Note

Sensitive credentials, session cookies, CSRF tokens, access tokens, and other authentication secrets should not be stored in the public repository.

Where authentication values are required, testers should use their own authorized test credentials and generate fresh session values.

## Evidence

API execution evidence and relevant screenshots may be stored separately in the repository evidence folders.

## Summary

The Postman collection provides repeatable API coverage for the main authentication, wallet, and transaction workflows tested during the AURIX QA evaluation.
