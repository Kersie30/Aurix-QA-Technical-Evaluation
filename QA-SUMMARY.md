# AURIX QA Technical Evaluation – QA Summary

## 1. Executive Summary

This QA evaluation was performed on the AURIX web application to assess its functional behaviour, API behaviour, security-related validation, performance, usability, and reliability.

Testing included manual functional testing, API testing using Postman, UI automation using Playwright with Python, and basic performance testing using Apache JMeter.

The evaluation identified working functionality as well as areas requiring improvement, particularly around input validation and transaction-related business rules.

---

## 2. Scope of Testing

The following areas were included:

- User registration
- User authentication
- Session and access behaviour
- User profile
- Dashboard
- Gold functionality
- Silver functionality
- ETF functionality
- Eligibility and subscription behaviour
- Investment workflows
- Transaction functionality
- API testing
- Basic security validation
- UI and responsive behaviour
- Performance testing

---

## 3. Testing Approach

### Manual Testing

35 structured test cases were prepared covering positive, negative, functional, validation, security-related, and UI scenarios.

Manual exploratory testing was also performed to identify behaviours that may not be covered by predefined test cases.

### API Testing

Postman was used to test API/web endpoints related to:

- Authentication
- Current-user/session behaviour
- Unauthorized access
- Invalid authentication
- Wallet buy operations
- Wallet sell operations
- Transaction history

The exported Postman collection is included in the `api-testing` directory.

### Automation Testing

Playwright with Python was used to automate selected authentication scenarios.

Automated scenarios included:

- Successful login
- Invalid login
- Empty login submission

The automation scripts and execution instructions are available in the `automation` directory.

### Performance Testing

Apache JMeter was used to perform a basic load test against the AURIX web application.

A 50-user test was executed against the homepage.

Observed results included:

- Virtual users: 50
- Samples: 50
- Average response time: 543 ms
- Minimum response time: 407 ms
- Maximum response time: 1827 ms
- Error rate: 0.00%
- Approximate throughput: 1 request/second

No request failures were observed during this test.

---

## 4. Key Defect Observation

One notable business-rule/input-validation issue identified during testing was that the Buy/Sell functionality allowed a practice gold transaction with a value of €0.00.

Expected behaviour:

The application should reject zero-value purchase transactions and require an amount greater than zero.

Observed behaviour:

The transaction was accepted and the application displayed:

`Bought gold with €0.00 (practice)`

This issue was documented in the bug report with supporting evidence.

---

## 5. Risk Assessment

Based on the testing performed, the following areas should receive particular attention before production use:

**Transaction Validation – Medium/High Risk**

Financial transaction inputs should have strict server-side validation, including minimum transaction amounts and invalid boundary values.

**Authentication and Session Security – High Importance**

Authentication, authorization, session handling, CSRF protection, and unauthorized access controls should continue to receive comprehensive security testing.

**Financial Calculations – High Importance**

Gold, silver, ETF, fees, balances, and transaction calculations should be thoroughly validated because calculation errors could directly affect users.

**API Security – High Importance**

API endpoints should enforce authentication and authorization independently of the user interface.

**Performance and Scalability – Further Testing Required**

The basic 50-user test produced no errors, but this was a limited evaluation. Larger load, stress, endurance, authenticated workflow, and transaction performance testing would be required before making production-scale performance conclusions.

---

## 6. Overall Assessment

The AURIX application provides a testable foundation across authentication, wallet, investment, and transaction-related functionality.

The evaluation demonstrated functioning workflows, while also identifying areas where validation and defensive controls can be strengthened.

Because AURIX handles financial and investment-related functionality, transaction integrity, authorization, input validation, data protection, and financial calculations should be treated as high-priority quality areas.

The testing performed during this evaluation should be considered targeted QA coverage rather than exhaustive certification of the platform.

---

## 7. Deliverables

The repository contains:

- `test-plan/` – QA Test Plan
- `test-cases/` – 35 structured test cases
- `bug-reports/` – Defect reports and evidence
- `api-testing/` – Postman API collection and documentation
- `automation/` – Playwright/Python automated tests
- `performance-testing/` – JMeter test plan/results and evidence
- `QA-SUMMARY.md` – Final QA evaluation summary

---

## 8. Tools Used

- Postman – API testing
- Playwright – UI automation
- Python – Automation scripting
- Apache JMeter – Performance testing
- Browser Developer Tools – Investigation and validation
- GitHub – Test artefact management and submission

---

## Conclusion

The evaluation combined manual, API, automation, performance, and exploratory testing to assess AURIX from multiple quality perspectives.

The most important recommendation is to continue strengthening transaction validation, authentication/authorization controls, and financial workflow testing before production-scale use.
