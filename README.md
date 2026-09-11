# AURIX QA Technical Evaluation

This repository contains the deliverables completed as part of the AURIX QA Technical Evaluation.

The evaluation covers manual functional testing, API testing, UI automation, performance testing, defect reporting, and risk assessment of the AURIX web application.

## Application Under Test

**Application:** AURIX  
**Web Application:** aurixapp.de  
**Testing Type:** End-to-End QA Technical Evaluation

## Testing Scope

The following areas were covered during the evaluation:

- User registration and authentication
- Login validation and session behaviour
- Dashboard and user profile
- Gold and silver trading functionality
- Wallet operations
- ETF and investment functionality
- Transaction behaviour
- Input validation
- API behaviour
- Security and authorization checks
- UI and usability
- Automated UI testing
- Performance testing
- Defect reporting
- Risk assessment

## Repository Structure

### test-plan/

Contains the overall QA test plan describing:

- Testing objectives
- Scope
- Test strategy
- Test environment
- Testing techniques
- Entry and exit criteria
- Risks and assumptions

### test-cases/

Contains **35 structured test cases** covering the main functional and non-functional areas of the AURIX application.

Test cases include:

- Test Case ID
- Module
- Test Scenario
- Preconditions
- Test Steps
- Expected Result
- Actual Result
- Status
- Priority
- Test Type
- Evidence / Notes

### bug-reports/

Contains defects identified during exploratory and functional testing.

Each defect includes:

- Bug ID
- Title
- Severity
- Priority
- Environment
- Preconditions
- Steps to Reproduce
- Expected Result
- Actual Result
- Evidence
- Reproducibility

One identified issue involved the trading functionality accepting a zero-value gold purchase instead of preventing the transaction through input validation.

### api-testing/

API testing was performed using **Postman**.

The exported Postman collection is included in this directory.

API coverage includes:

- Authentication
- Login behaviour
- Current-user requests
- Unauthorized requests
- Invalid authentication
- Wallet operations
- Buy transactions
- Sell transactions
- Transaction history

### automation/

UI automation was implemented using:

- Python
- Playwright
- Chromium

Automated scenarios include:

1. Successful login
2. Invalid login
3. Empty login validation

The automation scripts and instructions for running the tests are included in the automation directory.

### performance-testing/

Performance testing was performed using **Apache JMeter**.

A load test was executed against the AURIX web application using **50 virtual users**.

Observed results included:

- Samples: 50
- Average Response Time: 543 ms
- Minimum Response Time: 407 ms
- Maximum Response Time: 1827 ms
- Error Rate: 0.00%
- Throughput: approximately 1 request/second

The performance test plan and supporting evidence are included in this directory.

### QA-SUMMARY.md

Provides an overall summary of:

- Testing performed
- Coverage achieved
- Key observations
- Defects identified
- Automation coverage
- API testing
- Performance results
- Overall QA assessment

### RISK-ASSESSMENT.md

Contains the QA risk assessment for the AURIX application.

Particular attention was given to risks associated with:

- Authentication
- Authorization
- Financial transactions
- Input validation
- Wallet operations
- User data
- API security
- Performance and reliability

## Tools Used

- Postman – API testing
- Playwright – UI automation
- Python – Automation scripting
- Apache JMeter – Performance testing
- Chrome / Chromium – Browser testing
- GitHub – Test documentation and evidence management
- Microsoft Excel – Test case and performance test documentation

## Testing Approach

A risk-based testing approach was used.

Higher priority was given to functionality that could affect:

- Authentication and account access
- Financial transactions
- Wallet balances
- Trading operations
- User information
- Authorization
- Data integrity

Positive, negative, boundary, exploratory, API, automation, and performance testing techniques were applied where appropriate.

## Key QA Observation

The application demonstrates functional implementation across several important user journeys; however, financial and transaction-related functionality requires particularly strict validation.

For example, testing identified a case where a zero-value gold purchase could be accepted in the practice trading workflow.

Financial transaction inputs should be validated on both the client and server side before a transaction is accepted.

## Deliverables

This repository includes:

- QA Test Plan
- 35 Test Cases
- Bug Report(s)
- Postman API Collection
- Playwright Automation Tests
- JMeter Performance Test Documentation
- Performance Evidence
- QA Evaluation Summary
- Risk Assessment

## Conclusion

The evaluation used a combination of manual, API, automated, exploratory, and performance testing to assess the quality of the AURIX web application.

The testing focused particularly on high-risk fintech functionality such as authentication, wallet operations, trading, transactions, authorization, and input validation.

All findings and supporting QA artifacts are documented within this repository for review.
