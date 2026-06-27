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

**Final chunk count:** 688
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

**Model used:** all-MiniLM-L6-v2 (via sentence-transformers)

**Production tradeoff reflection:** For a real app used by thousands of students, I would think about switching to a more powerful embedding model like OpenAI's text-embedding-3-small. The model I'm using is free and fast, but it can only read 256 tokens at a time, so if a chunk is longer than that,
it gets cut off and some information is lost. I would also test whether better accuracy is actually worth slower speed for responses.

---

## Retrieval Test Results

<!-- Run these 3 queries through your retrieval system and record the top returned chunks.
     For at least 2 of the 3, explain why the returned chunks are relevant to the query.
     Results must be text — not screenshots. -->

**Query 1:** Is Natalie Linnell a tough grader?

Top returned chunks:
- "unnecessarily difficult though. Never! Choose it! She's not as bad as people say. God only knows how Natalie Linnell decided on teaching as a career" (natalie_linnell.txt, distance: 0.573)
- "Her style of coding is messy, dated, and unprofessional. The midterms and quizzes had low averages and weren't curved. 15 people dropped" (natalie_linnell.txt, distance: 0.660)
- "I had a disappointing experience with Professor Linnell. She doesn't seem to care about the student experience, uses outdated teaching methods" (natalie_linnell.txt, distance: 0.745)

Relevance explanation: All returned chunks come from natalie_linnell.txt and directly
address grading difficulty, exam structure, and student frustration. The chunks mention
low averages, no curves, and high drop rates which are all directly relevant to the
question about tough grading.

---

**Query 2:** Which SCU CS professor do students recommend more, Tran or Linnell?

Top returned chunks:
- "professor, one of my favorites so far at SCU. As well-intentioned as Linnell is, her upper divs are useless." (natalie_linnell.txt, distance: 0.519)
- "her courses. Linnell is simultaneously strict, unorganized, and vague with her grading criteria" (natalie_linnell.txt, distance: 0.581)
- "SCU do better!! Grading is really rough and very subjective. Feels like a high school class" (natalie_linnell.txt, distance: 0.688)

Relevance explanation: Results are dominated by Linnell's reviews because her name
appears more frequently in contexts involving recommendations and comparisons. This is
a known limitation of the retrieval system — comparison questions that span multiple
documents are harder to handle than single-professor queries. The generation step
synthesizes both professors' reviews into a complete answer.

---

**Query 3:** Is Robert Finocchio's Business class worth taking?

Top returned chunks:
- "This is probably the best professor you'll ever have, in terms of teaching you about actual business. Finocchio can tell..." (robert_finocchio.txt, distance: 0.589)
- "His knowledge and experience in the valley give him a fantastic insight into current business tactics and formalities." (robert_finocchio.txt, distance: 0.613)
- "experienced business professional and treats his students as such. Does not really use the textbook in his lectures" (robert_finocchio.txt, distance: 0.620)

Relevance explanation: All results come from robert_finocchio.txt with low distance
scores (0.589–0.620), indicating strong semantic matches. The chunks directly address
teaching quality, business knowledge, and student recommendations which are exactly
what the question asks about

---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:** "You are a helpful assistant that answers questions about SCU professors and courses
using only the student reviews provided to you. STRICT RULES: Answer only using
information from the provided documents. Do not use any outside knowledge or general
assumptions about professors. If the documents do not contain enough information to
answer the question, say exactly: 'I don't have enough information in my documents to
answer that.' Always refer to specific things students said in the reviews. Never make
up or infer information that isn't explicitly in the documents."

**How source attribution is surfaced in the response:** Source attribution is handled programmatically. After retrieval, the source filename
of each returned chunk is collected into a list. This list is appended
to the response separately in the Gradio interface under a "Retrieved from" field,
guaranteeing attribution even if the LLM forgets to cite sources in its answer.

---

## Example Responses

<!-- Provide at least 2 grounded responses (query + response + source attribution)
     and 1 out-of-scope query showing your system's refusal.
     All entries must be text — not screenshots. -->

**Grounded response 1**

Query: Is Natalie Linnell a tough grader?

Response: According to the reviews, Natalie Linnell is a tough grader. One student
mentioned that "The midterms and quizzes had low averages and weren't curved"
(natalie_linnell.txt), which suggests that her grading is strict. Another student
stated that "Her grading feels biased" (natalie_linnell.txt), implying they felt her
grading was unfair. Additionally, a student noted that "15 people dropped" the course
(natalie_linnell.txt), which indicates the high academic demands. However, one review
mentions she "teaches straight to the point and is extremely knowledgeable in her
subject" (natalie_linnell.txt).

Source attribution: natalie_linnell.txt

---

**Grounded response 2**

Query: Is Robert Finocchio worth taking for Business?

Response: According to the student reviews, Robert Finocchio is definitely worth
taking. One student said "If you have the chance to take him, do it!!!", indicating
a strong recommendation. Another student stated "He is a great teacher. Probably my
favorite freshman year teacher", showing high enthusiasm. Additionally, a student
mentioned "I got an A and loved the class", suggesting the class is both enjoyable
and rewarding. The reviews consistently praise Finocchio as knowledgeable and
experienced, with one student noting his "fantastic insight into current business
tactics" from his Silicon Valley background.

Source attribution: robert_finocchio.txt

---

**Out-of-scope query**

Query: What is the best restaurant I should eat at in Santa Clara?

System response (refusal): I don't have enough information in my documents to answer that.

---

## Query Interface

<!-- Describe your query interface: what are the input fields, what does the output look like?
     Then provide a complete sample interaction transcript showing a real exchange. -->

**Input fields:**  A single text box labeled "Your question" where the user types their question about an SCU professor or course.

**Output format:** Two text boxes: Answer" which contains the grounded response citing specific student reviews, and "Retrieved from" which lists the source files the answer was drawn from.

---

**Sample Interaction Transcript**

<!-- Show a complete query → response exchange as it actually appears in your interface.
     Must be text — not a screenshot. -->

> **User:** Is Natalie Linnell a tough grader?

> **System:** According to the reviews, Natalie Linnell is a tough grader. One student mentioned that "The midterms and quizzes had low averages and weren't curved" (natalie_linnell.txt), which suggests that her grading is strict. Another student stated that "Her grading feels biased" (natalie_linnell.txt), implying that they felt her grading was unfair. Additionally, a student noted that "15 people dropped" the course (natalie_linnell.txt), which could be indicative of a high level of difficulty or strict grading. However, it's worth noting that one review, although mostly negative, mentions that she "teaches straight to the point and is extremely knowledgeable in her subject" (natalie_linnell.txt), but this does not necessarily contradict the notion that she is a tough grader.
>
> Retrieved from: natalie_linnell.txt

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | Is Natalie Linnell a tough grader? | Students describe her grading as rough and subjective. Reviews mention mandatory attendance, cold calling, and daily homework. Only 22% of students would take her again. | System confirmed she is a tough grader, citing low exam averages, no curves, biased grading, and 15 students dropping the course. Also noted she is knowledgeable. | Relevant | Accurate | 
| 2 | Does Nicholas Tran curve his exams? |  Yes. Multiple reviews confirm he curves grades generously and provides practice exams before each midterm. However, exams are still considered tough and small mistakes can cost half the credit on a question, so the curve helps but doesn't make it easy. | System confirmed he curves based on mean and standard deviation, though the response got confused briefly by a Moataghed review that slipped into context before self-correcting. | Partially Relevant | Partially Accurate |
| 3 | Does Keyvan Moataghed give useful feedback on assignments? | Mostly yes. Students say his tests focus directly on lecture material, so if you attend and understand his slides you can pass without reading the textbook. He gives extra credit for answering questions in class. The course is lecture heavy and the material itself is hard, but the grading structure is manageable being two midterms, one final, two homeworks. | System said it did not have enough information, then partially answered by noting he is willing to help outside class and cares about students, but could not confirm feedback on assignments specifically. | Partially Relevant | Partially Accurate |
| 4 | Is Robert Finocchio's Business class worth taking? |  Yes. He has a 4.5 rating and 95% of students would take him again. Students highlight his real Silicon Valley executive experience, engaging lectures, and flexible office hours. Exams are drawn from assigned readings so you need to keep up, but students describe tests as manageable if you follow his study advice. | System confirmed strongly, citing multiple student quotes recommending him and describing him as one of the best professors for learning real-world business. | Relevant | Accurate |
| 5 | Which SCU CS professor do students recommend more, Tran or Linnell? | Nicholas Tran is more recommended. 54% of students would take him again vs only 19% for Linnell. Tran is described as caring and generous with curves. Linnell receives frequent criticism for subjective grading, cold calling, and disorganization, with some reviews saying she discouraged students from pursuing CS altogether. | System said it did not have enough information and only retrieved Linnell reviews, missing Tran entirely. Could not make the comparison. | Off-target | Inaccurate |


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
Which SCU CS professor do students recommend more, Tran or Linnell?

**What the system returned:**
The system said it did not have enough information to answer and only referenced
Linnell reviews, noting students said "I would not recommend choosing her as a
professor over other professors." There was no mention of Tran in the response
at all, showing how it did not even bother checking that document for information.

**Root cause (tied to a specific pipeline stage):**
The failure happened at the retrieval stage. The query "Which SCU CS professor do
students recommend more, Tran or Linnell?" contains both professor names, but the
embedding model converted the full query into a single vector that matched most
strongly against Linnell's reviews because her name appears far more frequently in
negative recommendation contexts. As a result, all 5 retrieved chunks came from
natalie_linnell.txt and none from nicholas_tran.txt. The generation stage then
correctly refused to compare two professors when it only had data on one, but
the root problem was that retrieval never surfaced Tran's reviews in the first place.

**What you would change to fix it:**
For comparison questions involving two named professors, I would decompose the query
into two separate retrievals one for each professor, then merge the results before
passing them to the LLM. For example, retrieve the top 3 chunks for "Natalie Linnell
recommendation" and the top 3 chunks for "Nicholas Tran recommendation" separately,
combine them into one context block, and then ask the LLM to compare. This would
guarantee both professors are represented in the context regardless of which name the
embedding model latches onto.

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:** Writing out my chunking strategy in planning.md before writing any code made me
think carefully about what my documents actually looked like. Because I had already noted that RMP reviews are short, I knew to pick a small chunk size of 300 tokens instead of just going with a large default. This paid off during implementation because my chunks ended up containing complete review sentences rather than random cut off fragments, which made retrieval work better. If I had skipped planning and just started coding, I probably would have used a default chunk size that was too large for short review text.

**One way your implementation diverged from the spec, and why:** My planning.md said I would use the Claude API for generation, but I ended up using
Groq's llama-3.3-70b-versatile instead. This happened because the project instructions recommended Groq as a free option that doesn't require a paid API key. The end result was the same, and was a model that follows grounding instructions and produces cited answers so the change didn't hurt anything
from what I originally planned.

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

- *What I gave the AI:* My Documents section and Chunking Strategy section from
  planning.md, asking it to implement an ingest.py script using requests,
  BeautifulSoup, and LangChain's RecursiveCharacterTextSplitter with 300 token
  chunks and 50 token overlap.
- *What it produced:* A working ingest.py that loaded .txt files, cleaned text
  using regex patterns, and split documents into chunks.
- *What I changed or overrode:* The initial clean_text function did not fully remove
  RMP boilerplate like "Thumbs up 0 Thumbs down 0" and tag words like "Tough grader"
  because the raw text had newlines between words that broke the regex patterns. I
  iteratively directed the AI to rewrite the cleaning function multiple times until
  the chunks contained mostly review text with minimal noise.

**Instance 2**

- *What I gave the AI:* My Retrieval Approach section and pipeline diagram, asking
  it to implement embed.py using sentence-transformers with all-MiniLM-L6-v2,
  ChromaDB for storage, and a retrieve() function returning top-5 chunks with
  distance scores.
- *What it produced:* A working embed.py that embedded all 688 chunks into ChromaDB
  with source metadata and a retrieval function that returned relevant chunks with
  distance scores.
- *What I changed or overrode:* Initial retrieval tests showed high distance scores
  for the Nicholas Tran query. I directed the AI to try larger chunk sizes (500
  tokens) and rephrased the test queries to be more natural. After testing both
  settings, I reverted to 300 token chunks because the larger size reduced total
  chunks from 688 to 431 without meaningfully improving distance scores, meaning
  less coverage for no benefit.
