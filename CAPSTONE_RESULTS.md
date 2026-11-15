# Capstone â€” Test Results

## Baseline Acceptance Criteria

| Criterion                     | Target                          | Observed Result | Verdict |
| ----------------------------- | ------------------------------- | --------------- | ------- |
| 1. Successful Request Logging | 10/10 valid log entries         | 10/10           | MET     |
| 2. Failed Request Logging     | 3/3 HTTP 400 and error logs     | 3/3             | MET     |
| 3. Response Time              | At least 9/10 within 10 seconds | 10/10           | MET     |
| 4. API Response Correctness   | 3/3 valid JSON responses        | 3/3             | MET     |
| 5. Server Health Check        | 3/3 healthy responses           | 3/3             | MET     |

## Response Time Measurement

Caching was disabled with `AI201_CACHE=0`.

Ten real Gemini requests completed successfully, with an average response time of 1.286 seconds.

An earlier cached test averaged 0.057 seconds. That result was not used as the real Gemini latency measurement.

## Measured Improvement â€” Invalid Input Handling

**Before:** Sending `{"question":123}` returned HTTP 500 without a corresponding structured error log. One baseline trial was observed.

**Change:** Updated `serve.py` to validate that the JSON payload is an object and the question is a string before calling `.strip()`.

**After:** Three invalid-input requests returned HTTP 400, and all three created structured error log entries.

**Verdict:** The observed failure was fixed in all three after-change trials.

## Cost Measurement

- Model: gemini-3.5-flash-lite
- Real Gemini API calls: 10
- Input tokens: 6,220
- Output tokens: 629
- Total tokens: 6,849

See `CAPSTONE_COST.md` for estimated costs.

## Remaining Limitations

- The service runs locally and has not been publicly deployed.
- The performance test used repeated questions rather than a diverse workload.
- Request logs contain full questions and answers.
- Token counters reset when the server restarts.
- The invalid-input improvement was tested with numeric questions; other malformed inputs need additional testing.
- Only one baseline invalid-input trial was recorded before the fix.

## Additional Observed Failure — Gemini Rate Limit

During repeated API testing, Gemini returned HTTP 429 RESOURCE_EXHAUSTED because the free-tier limit of 15 requests per minute was exceeded.

The Flask API recorded the failed request in logs/requests.jsonl with status "error" and duration_seconds 16.154.

This shows that structured error logging works for external API failures. However, the request itself was not recovered successfully. Future work should add rate-aware throttling or a controlled retry strategy.


## Additional Latency Analysis — Existing Logs

Thirty successful requests were selected retrospectively from the JSONL logs and divided into three consecutive groups of ten.

| Group | Target | Within 10 Seconds | Verdict |
|---|---|---|---|
| 1 | At least 9/10 | 10/10 | MET |
| 2 | At least 9/10 | 10/10 | MET |
| 3 | At least 9/10 | 9/10 | MET |

One request took 14.252 seconds. These groups were reconstructed from existing logs, not executed as three separately planned trials.


## Additional Successful Logging Analysis — Existing Logs

Thirty successful requests were selected retrospectively from the JSONL logs and divided into three consecutive groups of ten.

| Group | Target | Valid Log Entries | Verdict |
|---|---|---|---|
| 1 | 10/10 | 10/10 | MET |
| 2 | 10/10 | 10/10 | MET |
| 3 | 10/10 | 10/10 | MET |

Each entry contained timestamp, question, answer, duration_seconds, and status. These groups were reconstructed from existing logs rather than executed as three separately planned trials.

