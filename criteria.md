# Acceptance criteria — The Unofficial Guide

Five criteria that say what "working" means for this system, written in unit 1
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. "Retrieval works" is an opinion. "For at
least 4 of my 5 test questions, the top results include a chunk containing the
answer" is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter or looser one. A reason that says something about your corpus or your
pipeline earns credit; "80% seemed reasonable" does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## 1. Retrieved chunks contain the answer

For at least 4 of my 5 test questions, the retrieved chunks include one that
contains the answer.

**Why this target:**

I chose 4 out of 5 because the campus_life documents are short and usually
focus on one topic, so I expect retrieval to find the correct information for
most questions. I still allow one question to be missed because retrieval may
not always return the best matching chunk.

---

## 2. Every answer names a source

Every answer the system produces names at least one source document.

**Why this target:**

I chose this target because every generated answer should be grounded in the
retrieved documents. Naming at least one source makes it possible to check
where the answer came from and helps prevent unsupported answers.

---

## 3. The relevance gate stops out-of-corpus questions

When I ask a question my documents clearly don't cover, the relevance gate
stops it and the system returns "I don't have enough information about that" —
in at least 4 of 5 tries.

**Why this target:**

I chose 4 out of 5 because the out-of-scope questions are unrelated to the
campus_life documents, so most of them should be rejected by the relevance
gate. I allow one miss because similarity distances may sometimes overlap.

---

## 4. Chunks are complete and understandable

At least 4 out of 5 sampled chunks should contain enough context to be
understandable on their own without cutting important information in the
middle.

**Why this target:**

The campus_life documents are short and usually focus on a single topic.
Because of this, most chunks should preserve a complete idea, but I allow one
chunk to be imperfect because chunk boundaries may occasionally split related
information.

---

## 5. Answers stay grounded in the retrieved documents

For at least 4 out of my 5 test questions, the generated answer should not
include factual information that is unsupported by the retrieved documents.

**Why this target:**

The purpose of this RAG system is to answer questions using the campus_life
corpus instead of relying on unsupported model knowledge. I chose 4 out of 5
because I expect most answers to remain grounded while allowing one case where
the generated response may include extra information.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 2 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 1. Retrieved chunks contain the answer

         For at least 4 of my 5 test questions, the retrieved chunks include
         one that contains the answer.

         **Why this target:** ...

         > **Revised in unit 2:** For at least 4 of 5 questions, the top three
         > results contain the answer.
         >
         > **Why revised:** I couldn't judge "the chunks include one that
         > contains the answer" the same way twice — I scored two questions
         > differently on Monday than on Wednesday. The new version is
         > something I can actually check.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said 4 of 5 but got 2 of 5, so 2 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.

     The whole reason the originals stay visible is so someone can see what you
     said before you knew the answer.
     ───────────────────────────────────────────────────────────────────────── -->
