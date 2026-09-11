# AURIX QA Risk Assessment

## 1. Purpose

This risk assessment identifies key quality, security, functional, and performance risks observed or considered during the AURIX QA Technical Evaluation.

AURIX is a financial application involving authentication, wallets, precious-metal trading, transactions, and investment-related functionality. Therefore, transaction integrity, authentication, authorization, input validation, and protection of user data are considered high-risk areas.

## 2. Risk Rating

Risks are assessed using:

- Likelihood: Low / Medium / High
- Impact: Low / Medium / High / Critical
- Overall Risk: Low / Medium / High / Critical

## 3. Identified Risks

| ID | Risk | Likelihood | Impact | Overall Risk | Mitigation / Recommendation |
|---|---|---|---|---|---|
| RISK-01 | Invalid or zero-value financial transactions may be accepted | High | High | High | Implement server-side and client-side validation requiring transaction amounts greater than zero and within permitted limits. |
| RISK-02 | Authentication or session weaknesses could allow unauthorized account access | Medium | Critical | High | Enforce secure authentication, session expiration, secure cookies, MFA/2FA where applicable, and server-side authorization checks. |
| RISK-03 | Unauthorized users may attempt to access protected user or wallet information | Medium | Critical | High | Apply authorization checks to every protected endpoint and test against IDOR/BOLA vulnerabilities. |
| RISK-04 | Incorrect wallet calculations could affect balances or transaction records | Medium | Critical | High | Validate calculations server-side, use transaction integrity controls, and maintain auditable transaction records. |
| RISK-05 | Duplicate transaction submissions could create incorrect purchases or sales | Medium | High | High | Implement idempotency controls and disable repeated submission while a transaction is processing. |
| RISK-06 | Insufficient input validation could allow invalid financial data | High | High | High | Validate zero, negative, excessive, empty, malformed, and unsupported inputs on both client and server sides. |
| RISK-07 | Sensitive information could be exposed through API responses, logs, or repository files | Medium | High | High | Minimize API response data, mask sensitive information, exclude secrets and credentials from repositories, and use environment variables. |
| RISK-08 | Application performance may degrade under increased concurrent usage | Medium | Medium | Medium | Continue load and stress testing with realistic authenticated user journeys and monitor server resources. |
| RISK-09 | External market/pricing data may become unavailable or inaccurate | Medium | High | High | Validate data sources, implement error handling, monitoring, fallback behaviour, and timestamp displayed market prices. |
| RISK-10 | Browser/device differences may affect usability or transaction flows | Medium | Medium | Medium | Perform cross-browser, responsive, and mobile-device testing before production release. |

## 4. Risk-Based Testing Priorities

Based on the assessment, the highest testing priority should be given to:

1. Authentication and authorization
2. Financial transaction validation
3. Wallet balance and transaction integrity
4. API security and access control
5. Input and boundary-value validation
6. Protection of sensitive user information
7. Duplicate transaction prevention
8. Performance under concurrent usage

## 5. Observed Risk During Testing

During manual testing, the application accepted a gold purchase with a value of €0.00 in the practice trading environment.

The application displayed:

> "Bought gold with €0.00 (practice)"

This demonstrates an input/business-rule validation risk. A financial transaction should require a valid positive amount before it can be processed.

This issue has been documented separately in the bug report.

## 6. Performance Risk Observation

A JMeter test was executed against the AURIX web application using 50 simulated users.

Observed results included:

- Samples: 50
- Average response time: 543 ms
- Minimum response time: 407 ms
- Maximum response time: 1827 ms
- Error rate: 0.00%
- Throughput: approximately 1 request/second

No request failures were observed during this limited test.

However, this test should not be interpreted as proof of production-scale performance. Further load, stress, endurance, and authenticated transaction testing is recommended.

## 7. Overall Assessment

Overall application risk is assessed as **HIGH** because AURIX handles financial and user-account functionality where defects in authentication, authorization, transaction validation, wallet calculations, or data protection could have significant consequences.

The application demonstrated stable behavior during the limited performance test, but transaction validation and security controls should receive strong attention before production deployment.

## 8. Recommendation

Before production release, priority should be given to:

- Strengthening transaction input validation
- Performing deeper authentication and authorization testing
- Testing IDOR/BOLA scenarios using authorized test accounts
- Verifying wallet and transaction calculations
- Testing duplicate transaction protection
- Performing additional API security testing
- Expanding performance testing to realistic authenticated workflows
- Conducting cross-browser and responsive testing
- Completing regression testing after defect fixes

---

**Prepared as part of the AURIX QA Technical Evaluation**
