# Capstone Acceptance Criteria

## Criterion 1 — Successful Request Logging

**Target:** 10 out of 10 successful API requests must create a JSONL log entry with a timestamp, question, answer, duration, and status.

**Reason:** I added structured logging to my RAG API. I chose 10 out of 10 because every successful request should be recorded so I can track responses and measure performance.

## Criterion 2 — Failed Request Logging

**Target:** 3 out of 3 empty-question API requests must return HTTP 400 and create a JSONL log entry with status "error".

**Reason:** My RAG API should reject invalid questions and record these failures. I chose 3 out of 3 because this is a predictable error that the API should handle consistently.

## Criterion 3 — Response Time

**Target:** At least 9 out of 10 valid API requests must complete within 10 seconds.

**Reason:** My RAG system performs document retrieval and generates answers using Gemini. I chose 10 seconds because the API needs time for both operations, but users should not have to wait too long for a response.

## Criterion 4 — API Response Correctness

**Target:** 3 out of 3 valid API requests must return HTTP 200 with the fields question, answer, refused, sources, best_distance, threshold, and corpus.

**Reason:** My RAG API returns grounded answers along with source information. I chose 3 out of 3 because these response fields are required for clients to use the API correctly.

## Criterion 5 — Server Health Check

**Target:** 3 out of 3 requests to the /health endpoint must return HTTP 200 with status "ok", corpus name, and index_ready set to true.

**Reason:** My RAG API depends on the Chroma vector database. I chose 3 out of 3 because the health endpoint should consistently confirm that the server is running and the document index is available.
