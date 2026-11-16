# The Unofficial Guide

**Name:** Priyanka  
**Corpus:** `campus_life`

## Unit 1

### What This Does

The Unofficial Guide is a RAG-based question-answering system using the campus_life corpus. It answers questions about campus topics such as courses, housing, dining, parking, and student life. The system retrieves relevant information from the corpus and uses it to generate a grounded answer with source information. A relevance gate prevents the system from answering questions when the corpus does not contain enough relevant information.

### Chunking Strategy

Chunk size: One complete document per chunk

Overlap: None

I chose to keep each document as one complete chunk because the campus_life documents are short and usually focus on one topic. When I inspected five sample chunks, all five were understandable on their own without needing text from another chunk. Keeping each short post together preserves its context and avoids splitting useful information in the middle.

### Sample Chunks

**Chunk 1 — source: admin_add_drop_deadline.txt#0 — produced by: chunker.py::split_documents**

On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer
window — through the end of week six — but a drop after week two shows as a W
on your transcript. Nothing anywhere on the registrar's site says this plainly,
and students find out from each other.
**Chunk 2 — source: course_biol_160.txt#0 — produced by: chunker.py::split_documents**

BIOL 160 Cell Biology

I lived here my sophomore year. Format is lecture three times a week with a
weekly lab. Assessment: four unit tests and a cumulative final. Not curved.

Expect 9 to 11 hours a week, the heaviest first-year course by reputation.

The one piece of advice: the unit tests come fast, roughly every three weeks;
falling behind once is very hard to recover from.
**Chunk 3 — source: course_hist_118_workload.txt#0 — produced by: chunker.py::split_documents**

Workload for HIST 118 Modern World History

People keep asking so: a lot of reading, about 120 pages a week, but no problem
sets. That's real time, not optimistic time.

It's front-loaded — the first month is heavier than the rest, partly because
you're learning the format.
**Chunk 4 — source: dining_pellew_dining_hall_followup.txt#0 — produced by: chunker.py::split_documents**

Re: Pellew Dining Hall

Adding to what people have said about Pellew Dining Hall. The wait figure of
12 to 18 minutes at peak matches what I've seen. If you're trying to eat
between classes, go before 11:45 and it's a different building entirely.

Also worth saying: the furthest hall from anywhere, next to the athletics
centre. Nobody tells you this at orientation.
**Chunk 5 — source: housing_innisfree_hall.txt#0 — produced by: chunker.py::split_documents**

Innisfree Hall — what it's actually like

Transferred in last year, so take this with a grain of salt. Built 1991,
renovated 2022. Rooms are doubles arranged as pairs sharing one bathroom
between two rooms.

The good: the shared-bathroom-between-two-rooms arrangement is the best
compromise on campus.

The bad: no air conditioning, which matters for the first three weeks of
September.

Laundry costs $1.75 wash, $1.75 dry, app-based. On noise: moderate; the
building is L-shaped and the short wing is much quieter.

### Sample Answer

Question:

What material are the CS 210 exams based on?

Answer:

The CS 210 exams are drawn from lecture material rather than the textbook.

Sources:

- course_cs_210_exams.txt
- course_cs_210.txt

### Relevance Cutoff

My relevance cutoff: 0.6

I kept the relevance cutoff at 0.6 after comparing questions covered by the corpus with questions clearly outside the corpus. The five in-corpus questions had best distances between 0.180 and 0.402. The out-of-scope questions were farther away; for example, the Mongolia question had a distance of 0.825 and the diesel-engine question had a distance of 0.934. During my testing, the 0.6 cutoff correctly allowed all five in-corpus questions and rejected all five out-of-scope questions.

| Question                                                            | In corpus? | Best distance |
| ------------------------------------------------------------------- | ---------- | ------------- |
| What material are the CS 210 exams based on?                        | Yes        | 0.300         |
| What time should students go to The Atrium to avoid the lunch rush? | Yes        | 0.332         |
| What type of kitchen does Tamsin Court provide?                     | Yes        | 0.401         |
| When do student parking permits for the west lots go on sale?       | Yes        | 0.180         |
| By what time is The Atrium usually picked clean?                    | Yes        | 0.402         |
| What is the capital of Mongolia?                                    | No         | 0.825         |
| How do I change the oil in a diesel engine?                         | No         | 0.934         |
| Who won the 1994 World Cup?                                         | No         | 0.886         |
| What is the recommended dosage of ibuprofen for a headache?         | No         | 0.844         |
| How do I write a for loop in Rust?                                  | No         | 0.896         |

### How I Used AI

1. I used AI to help me understand the starter RAG pipeline and the role of document loading, chunking, embeddings, the vector store, retrieval, the relevance gate, and answer generation. I used the explanations to test each stage of the pipeline myself and understand the output.

2. I used AI to help me implement a chunking strategy based on my observations of the campus_life corpus. After inspecting the documents and five sample chunks, I chose to keep each short document as one complete chunk. I then tested the implementation and verified that the chunks were produced by chunker.py::split_documents.

I also tested five in-corpus and five out-of-scope questions. All five in-corpus questions were answered, while all five out-of-scope questions were rejected by the relevance gate.

## Unit 2

### Run Log — Before

| Criterion                                       | Target | Run 1 | Run 2 | Run 3 | Verdict |
| ----------------------------------------------- | ------ | ----- | ----- | ----- | ------- |
| 1. Retrieved chunk contains the answer          | 4 of 5 | 5/5   | 5/5   | 5/5   | MET     |
| 2. Every answer names a source                  | 5 of 5 | 5/5   | 5/5   | 5/5   | MET     |
| 3. Gate stops out-of-corpus questions           | 4 of 5 | 5/5   | 5/5   | 5/5   | MET     |
| 4. Chunks are complete and understandable       | 4 of 5 | 5/5   | 5/5   | 5/5   | MET     |
| 5. Answers stay grounded in retrieved documents | 4 of 5 | 5/5   | 5/5   | 5/5   | MET     |

### Real Output — Before

Produced by: run_eval.py::main
Retrieval: store.py::search
Chunks: chunker.py::split_documents

#### Criterion 1 — Retrieved chunk contains the answer

Question: What material are the CS 210 exams based on?

Best distance: 0.3002
Sources retrieved: course_cs_210.txt, course_cs_210_exams.txt, course_cs_340_exams.txt, course_engl_205.txt, course_engl_205_exams.txt

Actual answer:

The CS 210 exams are drawn from lecture material rather than the textbook.

Sources:

- course_cs_210_exams.txt
- course_cs_210.txt

#### Criterion 2 — Every answer names a source

Question: What time should students go to The Atrium to avoid the lunch rush?

Actual answer:

To avoid the lunch rush, students should go to The Atrium before 11:45.

Source: dining_the_atrium_followup.txt (and dining_the_atrium.txt)

#### Criterion 3 — Gate stops out-of-corpus questions

What is the capital of Mongolia? — refused — best distance 0.825
How do I change the oil in a diesel engine? — refused — best distance 0.934
Who won the 1994 World Cup? — refused — best distance 0.886
What is the recommended dosage of ibuprofen for a headache? — refused — best distance 0.844
How do I write a for loop in Rust? — refused — best distance 0.896

Gate refused 5 of 5.

#### Criterion 4 — Chunks are complete and understandable

Question: What type of kitchen does Tamsin Court provide?

Sources retrieved: dining_north_kitchen.txt, housing_fenwick_court.txt, housing_tamsin_court.txt, housing_tamsin_court_laundry.txt, housing_tamsin_court_noise.txt

Actual answer:

Tamsin Court provides a private kitchen in each studio apartment, and it is the only housing option on campus with a full kitchen.

This information comes from the document housing_tamsin_court.txt.

#### Criterion 5 — Answers stay grounded in retrieved documents

Question: When do student parking permits for the west lots go on sale?

Actual answer:

Student permits for the west lots go on sale in August (admin_parking_permits.txt).

### Verdicts

| #   | Criterion                                    | Verdict | How I decided                                                                                                             |
| --- | -------------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------- |
| 1   | Retrieved chunk contains the answer          | MET     | The retrieved chunks contained the expected answer for all 5 questions in all three runs, which met the target of 4 of 5. |
| 2   | Every answer names a source                  | MET     | All 5 answers named a source in all three runs, meeting the target of 5 of 5.                                             |
| 3   | Gate stops out-of-corpus questions           | MET     | The relevance gate refused all 5 out-of-corpus questions, which exceeded the target of 4 of 5.                            |
| 4   | Chunks are complete and understandable       | MET     | All 5 sampled chunks were complete and understandable on their own in all three runs, meeting the target of 4 of 5.       |
| 5   | Answers stay grounded in retrieved documents | MET     | All 5 answers stayed consistent with the retrieved documents in all three runs, meeting the target of 4 of 5.             |

### Diagnoses

None of my five criteria were missed. The system met the original targets in all three runs.

However, my targets for some criteria may have been a little low because the system consistently scored 5 out of 5. I would tighten Criterion 1, "Retrieved chunk contains the answer," from 4 of 5 to 5 of 5 in future testing.

One variation appeared in the generated answers. For the Tamsin Court question, run 3 said "private kitchen" instead of explicitly saying "full kitchen." The retrieved source still contained the correct information, and the answer stayed grounded in that source, but the wording did not include the expected phrase. This shows that answer generation can vary even when retrieval is consistent.

### The Improvement

What I changed:

I added one instruction to the grounding prompt in generate.py:

Preserve specific factual details and wording from the documents when they directly answer the question.

Why I picked it:

I chose this improvement because retrieval was working correctly, but the generated wording was not completely consistent. In the before evaluation, one Tamsin Court answer said only "private kitchen" instead of explicitly including the expected detail "full kitchen." Since the correct document was already being retrieved, I changed the answer-generation prompt rather than the retrieval system.

### Run Log — After

| Criterion                                       | Target | Run 1 | Run 2 | Run 3 | Verdict |
| ----------------------------------------------- | ------ | ----- | ----- | ----- | ------- |
| 1. Retrieved chunk contains the answer          | 4 of 5 | 5/5   | 5/5   | 5/5   | MET     |
| 2. Every answer names a source                  | 5 of 5 | 5/5   | 5/5   | 5/5   | MET     |
| 3. Gate stops out-of-corpus questions           | 4 of 5 | 5/5   | 5/5   | 5/5   | MET     |
| 4. Chunks are complete and understandable       | 4 of 5 | 5/5   | 5/5   | 5/5   | MET     |
| 5. Answers stay grounded in retrieved documents | 4 of 5 | 5/5   | 5/5   | 5/5   | MET     |

### Real Output — After

Produced by: run_eval.py::main
Retrieval: store.py::search
Chunks: chunker.py::split_documents

For the Tamsin Court question, the three generated answers were:

Run 1:

Based on the provided document, Tamsin Court provides rooms with a private kitchen (and a full kitchen).

Source: housing_tamsin_court.txt
Run 2:

Based on the provided document, Tamsin Court provides rooms with a private kitchen.

Source: housing_tamsin_court.txt
Run 3:

Tamsin Court rooms have a private kitchen (and a full kitchen).

Source: housing_tamsin_court.txt
The relevance gate also refused all 5 of 5 out-of-corpus questions.

Did it help?

The improvement made the prompt more explicit, but it did not completely remove the wording variation. Before the change, one of the three Tamsin Court runs omitted the phrase "full kitchen." After the change, one of the three runs still omitted it. Therefore, the improvement did not produce a measurable improvement on this three-run test.

The retrieval itself remained consistent, and all five original criteria continued to meet their targets.

### What's Still Broken

The main remaining issue is variation in answer generation. Even when the correct source is retrieved, the model may not include every specific phrase that is expected. For example, after the improvement, one Tamsin Court run still said "private kitchen" without explicitly saying "full kitchen."

The retrieval and relevance gate were consistent in these tests, but the generated wording can still vary between runs.

### What I'd Do Differently

If I continued working on the system, I would make the answer-generation step more structured instead of relying only on a general prompt instruction. For example, I would test a prompt that asks the model to first identify the exact fact in the retrieved document and then write the final answer from that fact.

I would also use more test questions and more repeated runs. Five questions with three runs each were enough to reveal some variation, but a larger test set would give stronger evidence about how reliable the system is.

### How I Used AI in Unit 2

I used AI to help organize the evaluation results into the criterion-level run log, understand the difference between retrieval performance and answer generation variation, and identify a focused prompt improvement. I reviewed the actual outputs before deciding whether each criterion was met and whether the improvement helped.

## Capstone

**What This Extends**

This capstone extends my existing The Unofficial Guide RAG application. The original project already supported document ingestion, semantic retrieval, a relevance gate, and grounded answers using Gemini. I extended its Flask API with structured request logging, performance measurements, token usage monitoring, and improved error handling.

**The Shape**

I selected Shape A: Deploy and Instrument, using Path B: a local HTTP service with logs. The application runs through Flask on port 5000. I chose this approach to demonstrate a working service and collect real operational measurements without requiring cloud hosting.

**Running It**

The project uses Python 3.13.7 and the dependencies in `requirements.txt`.

After installing dependencies and configuring the Gemini API key, build the index using `python app.py index`.

Start the service using:

`python serve.py`

The service exposes POST /ask, GET /health, and GET /usage.

For complete instructions, see `RUNNING.md`.

**Instrumentation**

Every /ask request records a timestamp, question, answer or error, processing duration, and status in `logs/requests.jsonl`.

I tested successful requests and validation failures. The /usage endpoint reports the number of Gemini calls and the input/output tokens used during the current server session.

#### Real Request Log Examples (10 entries)

The following examples are recorded JSONL entries, including successful requests and validation errors:

```jsonl
{"timestamp": "2026-11-15T07:35:07.109047+00:00", "question": "Is the housing lottery random?", "answer": "According to the documents, the housing lottery is not random in the way most people assume. Rising sophomores get a number drawn at random, but juniors and seniors are ordered by accumulated credit hours first, and only tie-break randomly. \n\n(Source: admin_housing_lottery.txt)", "duration_seconds": 0.689, "status": "success"}
{"timestamp": "2026-11-15T07:35:07.926682+00:00", "question": "Is the housing lottery random?", "answer": "Based on the provided documents, the housing lottery is not completely random in the way most people assume. While rising sophomores get a number drawn at random, juniors and seniors are ordered by accumulated credit hours first, and only tie-break randomly. \n\nDocument used: `admin_housing_lottery.txt`", "duration_seconds": 0.811, "status": "success"}
{"timestamp": "2026-11-15T07:35:08.741450+00:00", "question": "Is the housing lottery random?", "answer": "Based on the provided documents, the housing lottery is not completely random in the way most people assume. While rising sophomores get a number drawn at random, juniors and seniors are ordered by accumulated credit hours first, and only tie-break randomly. \n\nDocument used: `admin_housing_lottery.txt`", "duration_seconds": 0.805, "status": "success"}
{"timestamp": "2026-11-15T07:35:09.522344+00:00", "question": "Is the housing lottery random?", "answer": "Based on the provided documents, the housing lottery is not completely random in the way most people assume. While rising sophomores get a number drawn at random, juniors and seniors are ordered by accumulated credit hours first, and only tie-break randomly. \n\nDocument used: `admin_housing_lottery.txt`", "duration_seconds": 0.766, "status": "success"}
{"timestamp": "2026-11-15T07:35:10.293865+00:00", "question": "Is the housing lottery random?", "answer": "Based on the provided documents, the housing lottery is not completely random in the way most people assume: \"Rising sophomores get a number drawn at random, but juniors and seniors are ordered by accumulated credit hours first, and only tie-break randomly.\"\n\nSource file: admin_housing_lottery.txt", "duration_seconds": 0.762, "status": "success"}
{"timestamp": "2026-11-15T07:35:11.270956+00:00", "question": "Is the housing lottery random?", "answer": "Based on the provided documents, the housing lottery is not completely random in the way most people assume. While rising sophomores get a number drawn at random, juniors and seniors are ordered by accumulated credit hours first, and only tie-break randomly. \n\nDocument used: `admin_housing_lottery.txt`", "duration_seconds": 0.968, "status": "success"}
{"timestamp": "2026-11-15T07:35:11.938556+00:00", "question": "Is the housing lottery random?", "answer": "Based on the provided documents, the housing lottery is not completely random in the way most people assume: \"Rising sophomores get a number drawn at random, but juniors and seniors are ordered by accumulated credit hours first, and only tie-break randomly.\"\n\nSource: admin_housing_lottery.txt", "duration_seconds": 0.66, "status": "success"}
{"timestamp": "2026-11-15T07:41:54.711503+00:00", "question": "", "answer": "Missing or empty question", "duration_seconds": 0.017, "status": "error"}
{"timestamp": "2026-11-15T07:41:54.734914+00:00", "question": "", "answer": "Missing or empty question", "duration_seconds": 0.0, "status": "error"}
{"timestamp": "2026-11-15T07:41:54.739827+00:00", "question": "", "answer": "Missing or empty question", "duration_seconds": 0.0, "status": "error"}
```

**What It Costs**

I measured 10 real Gemini calls with caching disabled.

Input tokens: 6,220
Output tokens: 629
Total tokens: 6,849
Average cost per request: approximately $0.000344
Estimated cost at 100 requests/day: approximately $0.0344/day
These are estimated paid-tier API costs based on measured token counts, not actual billed charges. Hosting costs are excluded.

See `CAPSTONE_COST.md` for details.

**Run Log and Verdicts**

| Criterion                  | Target                          | Observed initial batch | Verdict |
| -------------------------- | ------------------------------- | ---------------------- | ------- |
| Successful request logging | 10/10                           | 10/10                  | MET     |
| Failed request logging     | 3/3                             | 3/3                    | MET     |
| Response time              | At least 9/10 within 10 seconds | 10/10                  | MET     |
| API response correctness   | 3/3                             | 3/3                    | MET     |
| Server health check        | 3/3                             | 3/3                    | MET     |

The initial 10-request uncached batch averaged 1.286 seconds. This is separate from the retrospective latency groups below.

The earlier cached test averaged 0.057 seconds and was excluded from the uncached performance result.

Detailed results are in `CAPSTONE_RESULTS.md`.

#### Additional Verified Trial Results — November 15, 2026

| Criterion                     | Target                   | Run 1                    | Run 2                    | Run 3                    | Verdict                     |
| ----------------------------- | ------------------------ | ------------------------ | ------------------------ | ------------------------ | --------------------------- |
| 1. Successful request logging | 10/10                    | 10/10                    | 10/10                    | 10/10                    | MET (retrospective groups)  |
| 2. Failed request logging     | 3/3                      | Not separately recorded  | Not separately recorded  | 3/3 in one batch         | MET for observed batch only |
| 3. Response time              | At least 9/10 within 10s | 10/10                    | 10/10                    | 9/10                     | MET (retrospective groups)  |
| 4. API response correctness   | 3/3                      | HTTP 200, fields present | HTTP 200, fields present | HTTP 200, fields present | MET for three requests      |
| 5. Server health check        | 3/3                      | `ok`, ready              | `ok`, ready              | `ok`, ready              | MET for three checks        |

The logging and latency results were reconstructed from existing successful-request logs in three groups of ten; they were not three separately scheduled trials. The failed-request results represent one observed batch of three requests. The API response and health checks were observed as three individual requests each, not three batches of three.

One successful request in the latency sample took **14.252 seconds**. Separately, a Gemini provider rate-limit error (HTTP 429) was observed during burst testing and logged as an error with a **16.154-second** duration. The latter is not included in the successful-request latency groups.

**Evidence limitation:** Before the invalid-input fix, one numeric-input trial returned HTTP 500 without a structured log. After the fix, three numeric-input trials returned HTTP 400 with structured error logs. A complete set of three before and three after trials for each of the five criteria was **not** performed. No unobserved trial results are claimed.

**The Improvement**

I identified an invalid-input handling problem in the Flask API.

Before the change, one recorded numeric-input test (`{"question":123}`) returned HTTP 500 without creating a structured error log.

I updated `serve.py` to validate the JSON payload and question type before processing.

After the change, three recorded numeric-input tests returned HTTP 400 and generated structured error logs.

This improvement made invalid-input handling more predictable and improved error traceability.

**What's Still Broken**

The application is running locally rather than on a public hosting service. Request logs contain full questions and answers, so they are not suitable for sensitive information without additional privacy protections.

The current token counters reset after a server restart. Performance measurements were based on a limited workload, and additional testing is needed for other malformed inputs. A Gemini rate-limit failure was observed during burst testing; request throttling or backoff would be a priority for future work. Complete three-trial before-and-after evidence for all five capstone criteria has not been collected.

**How I Used AI**

I used AI to help understand the Flask API, add structured logging, troubleshoot Python dependency issues, design testing commands, interpret actual test outputs, calculate estimated API costs, and organize the capstone documentation.

I ran the commands in my own environment, checked the API responses and logs, and used the observed results to document the improvement and remaining limitations. For example, I used AI to help interpret the numeric-input HTTP 500 failure, then verified the HTTP 400 behavior after adding validation. I also used AI to help organize the latency measurements, and checked the logged durations before reporting the results.
