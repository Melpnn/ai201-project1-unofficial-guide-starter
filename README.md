# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

SCU professor and course reviews: CS/Engineering and Business departments

This knowledge is valuable because the official course catalog tells you what a class covers, but not what the experience with the professor is like. Students rely on word of mouth from peers to find out whether a professor grades harshly and what an exam actually looks like. This informal knowledge exists but is scattered across Rate My Professors, student newspapers, and forums all over the internet. 

---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

| # | Source | Description | URL or location |
|---|--------|-------------|-----------------|
| 1 | Rate My Professor | Reviews for Natalie Linnell (CS) | https://www.ratemyprofessors.com/professor/1803411 |
| 2 | Rate My Professor | Reviews for Nicholas Tran (CS)| https://www.ratemyprofessors.com/professor/417798 |
| 3 | Rate My Professor | Reviews for Keyvan Moataghed (CS) | https://www.ratemyprofessors.com/professor/992788 |
| 4 | Rate My Professor | Reviews for Sumana Sur (Business) | https://www.ratemyprofessors.com/professor/125677 |
| 5 | Rate My Professor | Reviews for Michael Santoro (Business)  | https://www.ratemyprofessors.com/professor/2220418 |
| 6 | Rate My Professor | Reviews for Robert Finocchio (Business) | https://www.ratemyprofessors.com/professor/135191 |
| 7 | Rate My Professor | Reviews for Ramin Moazzeni (CS) | https://www.ratemyprofessors.com/professor/1984940 |
| 8 | Rate My Professor | Reviews for Amr Elkady (CS) | https://www.ratemyprofessors.com/professor/1996092 |
| 9 | Rate My Professor | Reviews for Michele Goins (CS) | https://www.ratemyprofessors.com/professor/1663424 |
| 10 | Poets&Quants | Review for Esther Sackett (Business) | https://poetsandquantsforundergrads.com/news/2022-best-undergraduate-professors-esther-sackett-santa-clara-university-leavey-school-of-business/ |

---

## Chunking Strategy

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:** 300 tokens

**Overlap:** 50 tokens

**Why these choices fit your documents:** Most of my sources are RMP reviews, which are short being 2 - 5 sentences each. A 300 token chunk should hold 1 – 3 complete reviews together and keep the full context of each student opinion without merging reviews into one chunk. I will overlap 50 tokens since one student's review doesn't really continue into the next student's review, so I don't need a lot of overlap. This is to ensure that if a review gets split across two chunks, the key sentence isn't lost entirely. I will split longer documents like the Poets&Quants article into more chunks.

**Final chunk count:**
688
---

## Sample Chunks

<!-- Paste 5 representative chunks from your document collection after running your ingestion pipeline.
     For each chunk, note which source document it came from.
     These must be actual text — not screenshots. -->

| # | Source document | Chunk text |
|---|----------------|------------|
| 1 | amir.txt | Amr Elkady Computer Science Santa Clara University Mandatory Always refer to class notes. Never forget to revise everything. Please pay attention in his lectures. You will receive all the answers you seek in class. Mandatory The professor is very good and straightforward. Read the class guidelines |
| 2 | amir.txt | and straightforward. Read the class guidelines and you are good to go. Professor Elkady is one of the few professors in SCU that actually cares about the students. He ensures that you receive a constant feedback regarding your progress in class. Class: assignment heavy, worth the cause. You learn a |
| 3 | amir.txt | assignment heavy, worth the cause. You learn a lot from the course. This is one of the reason he's the best professor & has received an award from the college too. Mandatory Good professor, would take again! One of the best course to learn things we all wish to accomplish as a graduate student. You |
| 4 | amir.txt | all wish to accomplish as a graduate student. You will understand how to build, develop and maintain web servers at the very foundational level which is very important. You will hardly learn such important concepts out in the industry. I will recommend all to take this course. teacher. Professor |
| 5 | amir.txt | all to take this course. teacher. Professor has a clear flow of all the topics and ensures you understand every aspect of the syllabus. Attendance is mandatory, but you will enjoy attending the classes (So not an issue). Feedback helps you to keep up with your classmates. Overall, a good professor |

---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:**

**Production tradeoff reflection:**

---

## Retrieval Test Results

<!-- Run these 3 queries through your retrieval system and record the top returned chunks.
     For at least 2 of the 3, explain why the returned chunks are relevant to the query.
     Results must be text — not screenshots. -->

**Query 1:**

Top returned chunks:
-
-
-

Relevance explanation:

---

**Query 2:**

Top returned chunks:
-
-
-

Relevance explanation:

---

**Query 3:**

Top returned chunks:
-
-
-

Relevance explanation:

---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:**

**How source attribution is surfaced in the response:**

---

## Example Responses

<!-- Provide at least 2 grounded responses (query + response + source attribution)
     and 1 out-of-scope query showing your system's refusal.
     All entries must be text — not screenshots. -->

**Grounded response 1**

Query:

Response:

Source attribution:

---

**Grounded response 2**

Query:

Response:

Source attribution:

---

**Out-of-scope query**

Query:

System response (refusal):

---

## Query Interface

<!-- Describe your query interface: what are the input fields, what does the output look like?
     Then provide a complete sample interaction transcript showing a real exchange. -->

**Input fields:**

**Output format:**

---

**Sample Interaction Transcript**

<!-- Show a complete query → response exchange as it actually appears in your interface.
     Must be text — not a screenshot. -->

> **User:** 

> **System:** 

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed:**

**What the system returned:**

**Root cause (tied to a specific pipeline stage):**

**What you would change to fix it:**

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**

**One way your implementation diverged from the spec, and why:**

---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*

**Instance 2**

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*
