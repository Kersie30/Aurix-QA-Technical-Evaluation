# AURIX QA Technical Evaluation – Demo Walkthrough

## Candidate
Keresia Karuma

## Purpose

This document provides a written walkthrough of the QA work completed during the AURIX Technical Evaluation.

Due to limitations in my current environment, I was unable to provide the requested 5-minute recorded demo. I have therefore provided this written walkthrough together with the supporting test documentation, scripts, results, screenshots, and evidence available in this repository.

---

## 1. Testing Approach

I used a risk-based testing approach, focusing primarily on the areas most important to a financial application, including:

- Authentication and access control
- User registration and login
- Trading functionality
- Wallet and transaction operations
- Input validation
- API behaviour
- Security and authorization
- Performance
- User experience and error handling

A structured test plan and 35 test cases were created before and during test execution.

---

## 2. Manual Testing

Manual functional and exploratory testing was performed on the AURIX web application.

Testing covered areas including:

- Registration
- Login and logout
- Authentication
- User profile
- Dashboard
- Gold trading
- Silver trading
- ETF functionality
- Wallet operations
- Transactions
- Input validation
- Access control
- General UI behaviour

Positive, negative and boundary scenarios were considered where applicable.

One notable issue identified during testing was that the application allowed a gold purchase with a value of €0.00 in the practice trading environment.

Instead of preventing the transaction, the application displayed:

"Bought gold with €0.00 (practice)"

The expected behaviour is for the application to reject a zero-value transaction and require the user to enter an amount greater than zero.

The defect and supporting screenshot are included in the repository.

---

## 3. API Testing

API testing was performed using Postman.

The Postman collection contains requests covering authentication and application functionality, including:

- Login page request
- Valid login
- Invalid/wrong password login
- Current authenticated user
- Unauthorized current-user request
- Buy transaction
- Sell transaction
- Transaction history

Both positive and negative scenarios were tested where applicable.

The Postman collection has been exported and included in the `api-testing` directory so the requests can be reviewed and reused.

Supporting API testing screenshots are also included in the evidence.

---

## 4. Test Automation

Playwright with Python was used to automate selected authentication scenarios.

Three automated tests were created:

1. Valid login
2. Invalid password/login
3. Empty login submission

The automation scripts are available in the `automation` directory.

These tests demonstrate how repetitive regression scenarios could be automated and extended as the AURIX application develops.

Screenshots/results from the automation execution are included as supporting evidence.

---

## 5. Performance Testing

Apache JMeter was used to perform a basic performance test against the AURIX web application.

The main performance scenario simulated:

- 50 users
- 50-second ramp-up period
- 1 iteration per user
- HTTP GET request to the AURIX application

Observed results included:

- Samples: 50
- Average response time: approximately 543 ms
- Minimum response time: approximately 407 ms
- Maximum response time: approximately 1827 ms
- Error rate: 0.00%
- Throughput: approximately 1 request/second

The test completed without request failures under this limited test scenario.

These results should be treated as an initial performance indication rather than a full production load or stress test.

The JMeter test information and evidence are available in the `performance-testing` directory.

---

## 6. Defect Reporting

Defects identified during testing were documented using structured bug reports.

Bug reports include:

- Bug ID
- Title
- Severity
- Priority
- Environment
- Preconditions
- Steps to reproduce
- Expected result
- Actual result
- Evidence
- Reproducibility

Severity was assigned according to the actual impact observed and was not intentionally inflated.

---

## 7. Risk Assessment

A separate risk assessment was prepared for the application.

Higher-risk areas considered include:

- Authentication and authorization
- Financial transaction validation
- Wallet and trading operations
- User data protection
- Access control
- Transaction integrity
- Performance and availability

For a financial application, these areas should receive continued regression, API, security and performance testing before production release.

---

## 8. Test Evidence

Supporting evidence has been included in the repository for the testing performed.

The evidence includes examples from:

- Manual testing
- API testing
- Playwright automation
- Performance testing
- Identified defects

This allows the test execution and findings described in the documentation to be independently reviewed.

---

## 9. Overall QA Assessment

The evaluation demonstrated that the AURIX application contains functioning core features that can be tested through the UI and API.

However, validation and financial transaction controls require particular attention. The observed ability to process a €0.00 practice gold transaction demonstrates the importance of stronger boundary and business-rule validation.

For future testing, I would expand coverage around:

- Transaction boundaries
- Authorization and access control
- Duplicate transactions
- Session management
- Wallet balances
- Financial calculations
- Security testing
- API validation
- Higher-load performance testing
- End-to-end regression automation

---

## Repository Deliverables

The repository contains:

- Test Plan
- 35 Test Cases
- Bug Reports
- Postman API Collection
- Playwright Automation Scripts
- JMeter Performance Testing
- Risk Assessment
- QA Summary
- Test Evidence
- Written Demo Walkthrough

## Conclusion

This evaluation combined manual, API, automation and performance testing to provide a risk-focused assessment of the AURIX application.

All findings and conclusions in this submission are based on the behaviour observed during the evaluation and the evidence collected during testing.
