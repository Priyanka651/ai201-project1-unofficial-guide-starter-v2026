# The Unofficial Guide

**Name:** Priyanka  
**Corpus:** campus_life

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video.

---

# Unit 1

## What This Does

The Unofficial Guide is a RAG-based question-answering system using the
`campus_life` corpus. It answers questions about campus topics such as courses,
housing, dining, parking, and student life. The system retrieves relevant
information from the corpus and uses it to generate a grounded answer with
source information. A relevance gate prevents the system from answering
questions when the corpus does not contain enough relevant information.

## Chunking Strategy

**Chunk size:** One complete document per chunk

**Overlap:** None

I chose to keep each document as one complete chunk because the `campus_life`
documents are short and usually focus on one topic. When I inspected five
sample chunks, all five were understandable on their own without needing text
from another chunk. Keeping each short post together preserves its context and
avoids splitting useful information in the middle.

## Sample Chunks

**Chunk 1** — source: `admin_add_drop_deadline.txt#0` — produced by: `chunker.py::split_documents`

```text
On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer
window — through the end of week six — but a drop after week two shows as a W
on your transcript. Nothing anywhere on the registrar's site says this plainly,
and students find out from each other.
```

**Chunk 2** — source: `course_biol_160.txt#0` — produced by: `chunker.py::split_documents`

```text
BIOL 160 Cell Biology

I lived here my sophomore year. Format is lecture three times a week with a
weekly lab. Assessment: four unit tests and a cumulative final. Not curved.

Expect 9 to 11 hours a week, the heaviest first-year course by reputation.

The one piece of advice: the unit tests come fast, roughly every three weeks;
falling behind once is very hard to recover from.
```

**Chunk 3** — source: `course_hist_118_workload.txt#0` — produced by: `chunker.py::split_documents`

```text
Workload for HIST 118 Modern World History

People keep asking so: a lot of reading, about 120 pages a week, but no problem
sets. That's real time, not optimistic time.

It's front-loaded — the first month is heavier than the rest, partly because
you're learning the format.
```

**Chunk 4** — source: `dining_pellew_dining_hall_followup.txt#0` — produced by: `chunker.py::split_documents`

```text
Re: Pellew Dining Hall

Adding to what people have said about Pellew Dining Hall. The wait figure of
12 to 18 minutes at peak matches what I've seen. If you're trying to eat
between classes, go before 11:45 and it's a different building entirely.

Also worth saying: the furthest hall from anywhere, next to the athletics
centre. Nobody tells you this at orientation.
```

**Chunk 5** — source: `housing_innisfree_hall.txt#0` — produced by: `chunker.py::split_documents`

```text
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
```

## Sample Answer

**Question:**

What material are the CS 210 exams based on?

**Answer:**

```text
The CS 210 exams are drawn from lecture material rather than the textbook.

Sources:
- course_cs_210_exams.txt
- course_cs_210.txt
```

## Relevance Cutoff

**My relevance cutoff:** `0.6`

I kept the relevance cutoff at 0.6 after comparing questions covered by the
corpus with questions clearly outside the corpus. The five in-corpus questions
had best distances between 0.180 and 0.402. The out-of-scope questions were
farther away; for example, the Mongolia question had a distance of 0.825 and
the diesel-engine question had a distance of 0.934. During my testing, the
0.6 cutoff correctly allowed all five in-corpus questions and rejected all
five out-of-scope questions.

| Question                                                            | In corpus? | Best distance |
| ------------------------------------------------------------------- | ---------- | ------------: |
| What material are the CS 210 exams based on?                        | Yes        |         0.300 |
| What time should students go to The Atrium to avoid the lunch rush? | Yes        |         0.332 |
| What type of kitchen does Tamsin Court provide?                     | Yes        |         0.401 |
| When do student parking permits for the west lots go on sale?       | Yes        |         0.180 |
| By what time is The Atrium usually picked clean?                    | Yes        |         0.402 |
| What is the capital of Mongolia?                                    | No         |         0.825 |
| How do I change the oil in a diesel engine?                         | No         |         0.934 |
| Who won the 1994 World Cup?                                         | No         |         0.886 |
| What is the recommended dosage of ibuprofen for a headache?         | No         |         0.844 |
| How do I write a for loop in Rust?                                  | No         |         0.896 |

## How I Used AI

**1.** I used AI to help me understand the starter RAG pipeline and the role
of document loading, chunking, embeddings, the vector store, retrieval, the
relevance gate, and answer generation. I used the explanations to test each
stage of the pipeline myself and understand the output.

**2.** I used AI to help me implement a chunking strategy based on my
observations of the `campus_life` corpus. After inspecting the documents and
five sample chunks, I chose to keep each short document as one complete chunk.
I then tested the implementation and verified that the chunks were produced by
`chunker.py::split_documents`.

---

# Unit 2

> Unit 2 will be completed after the Unit 1 system is finished. The Unit 1
> sections above should not be deleted or rewritten during Unit 2.

## Run Log — Before

| Criterion                                       | Target | Run 1 | Run 2 | Run 3 | Verdict |
| ----------------------------------------------- | ------ | ----- | ----- | ----- | ------- |
| 1. Retrieved chunk contains the answer          | 4 of 5 |       |       |       |         |
| 2. Every answer names a source                  | 5 of 5 |       |       |       |         |
| 3. Gate stops out-of-corpus questions           | 4 of 5 |       |       |       |         |
| 4. Chunks are complete and understandable       | 4 of 5 |       |       |       |         |
| 5. Answers stay grounded in retrieved documents | 4 of 5 |       |       |       |         |

## Verdicts

| #   | Criterion | Verdict | How I decided |
| --- | --------- | ------- | ------------- |
| 1   |           |         |               |
| 2   |           |         |               |
| 3   |           |         |               |
| 4   |           |         |               |
| 5   |           |         |               |

## Diagnoses

To be completed in Unit 2 after running the evaluation.

## The Improvement

**What I changed:**

**Why I picked it:**

### Run Log — After

| Criterion                                       | Target | Run 1 | Run 2 | Run 3 | Verdict |
| ----------------------------------------------- | ------ | ----- | ----- | ----- | ------- |
| 1. Retrieved chunk contains the answer          | 4 of 5 |       |       |       |         |
| 2. Every answer names a source                  | 5 of 5 |       |       |       |         |
| 3. Gate stops out-of-corpus questions           | 4 of 5 |       |       |       |         |
| 4. Chunks are complete and understandable       | 4 of 5 |       |       |       |         |
| 5. Answers stay grounded in retrieved documents | 4 of 5 |       |       |       |         |

**Did it help?**

To be completed in Unit 2.

## What's Still Broken

To be completed in Unit 2.

## What I'd Do Differently

To be completed in Unit 2.
