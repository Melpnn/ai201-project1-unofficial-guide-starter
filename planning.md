# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

<!-- What domain did you choose? Why is this knowledge valuable and hard to find through official channels? -->
SCU professor and course reviews: CS/Engineering and Business departments

This knowledge is valuable because the official course catalog tells you what a class covers, but not what the experience with the professor is like. Students rely on word of mouth from peers to find out whether a professor grades harshly and what an exam actually looks like. This informal knowledge exists but is scattered across Rate My Professors, student newspapers, and forums all over the internet. 

---

## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->

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

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

Chunk size: 300 tokens

Overlap: 50 tokens

Reasoning: Most of my sources are RMP reviews, which are short being 2 - 5 sentences each. A 300 token chunk should hold 1 – 3 complete reviews together and keep the full context of each student opinion without merging reviews into one chunk. I will overlap 50 tokens since one student's review doesn't really continue into the next student's review, so I don't need a lot of overlap. This is to ensure that if a review gets split across two chunks, the key sentence isn't lost entirely. I will split longer documents like the Poets&Quants article into more chunks.

---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

Embedding model: all-MiniLM-L6-v2 (via sentence-transformers)

Top-k: 5

Production tradeoff reflection: For a real app used by thousands of students, I would think about switching to a more powerful embedding model like OpenAI's text-embedding-3-small. The model I'm using is free and fast, but it can only read 256 tokens at a time, so if a chunk is longer than that,
it gets cut off and some information is lost. I would also test whether better accuracy is actually worth slower speed for responses.

---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

 # | Question | Expected answer |
|---|----------|-----------------|
| 1 | Is Natalie Linnell a tough grader? | Students describe her grading as rough and subjective. Reviews mention mandatory attendance, cold calling, and daily homework. Only 22% of students would take her again. |
| 2 | Does Nicholas Tran curve his exams? |  Yes. Multiple reviews confirm he curves grades generously and provides practice exams before each midterm. However, exams are still considered tough and small mistakes can cost half the credit on a question, so the curve helps but doesn't make it easy. |
| 3 | Does Keyvan Moataghed give useful feedback on assignments? | Mostly yes. Students say his tests focus directly on lecture material, so if you attend and understand his slides you can pass without reading the textbook. He gives extra credit for answering questions in class. The course is lecture heavy and the material itself is hard, but the grading structure is manageable being two midterms, one final, two homeworks. |
| 4 | Is Robert Finocchio's Business class worth taking? |  Yes. He has a 4.5 rating and 95% of students would take him again. Students highlight his real Silicon Valley executive experience, engaging lectures, and flexible office hours. Exams are drawn from assigned readings so you need to keep up, but students describe tests as manageable if you follow his study advice. |
| 5 | Which SCU CS professor do students recommend more, Tran or Linnell? | Nicholas Tran is more recommended. 54% of students would take him again vs only 19% for Linnell. Tran is described as caring and generous with curves. Linnell receives frequent criticism for subjective grading, cold calling, and disorganization, with some reviews saying she discouraged students from pursuing CS altogether. |

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1. The system could end up with polarizing results, since students who had either extremely bad or extremely good circumstances are more likely to write a review than an average one who had no real complaints or compliments. This means the data the system is collecting may not represent the typical experience of a student there.

2. Most SCU professors won't appear in the knowledge base at all. A student asking about a professor outside won't recieve a good response. The system needs to say something like "I don't have information about that professor" rather than hallucinate a response from unrelated chunks.

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->

        [Document Ingestion]
        requests + BeautifulSoup
        Fetches raw HTML from each
        source URL, extracts review text
                |
                v
            [Chunking]
        LangChain RecursiveCharacterTextSplitter
        Splits text into 300-token chunks
        with 50-token overlap
                |
                v
            [Embedding]
        all-MiniLM-L6-v2
        Converts each chunk into a vector
        capturing its meaning
                |
                v
          [Vector Store]
             ChromaDB
        Stores all chunk vectors
        for fast semantic search
                |
                v
            [Retrieval]
        ChromaDB semantic search
        Finds the top-5 most relevant
        chunks for the user's query
                |
                v
           [Generation]
        Groq / llama-3.3-70b-versatile
        Uses retrieved chunks as context
        to produce a grounded, cited answer
                |
                v
          [Interface]
            Gradio Web UI
        User enters a question,
        sees answer and source attribution
---

## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->

**Milestone 3 — Ingestion and chunking:**
I will give Claude my Documents section and Chunking Strategy section from this
planning.md and ask it to implement an ingest.py script that uses requests and
BeautifulSoup to fetch each URL, extracts the review text, cleans out HTML tags
and boilerplate, and splits the result into chunks using LangChain's
RecursiveCharacterTextSplitter with a chunk size of 300 tokens and 50-token overlap.
I will verify the output by printing 5 chunks and checking they look like complete,
readable review sentences with no HTML artifacts or fragments.

**Milestone 4 — Embedding and retrieval:**
I will give Claude my Retrieval Approach section and pipeline diagram and ask it to
implement an embed.py script that loads chunks from ingest.py, generates embeddings
using sentence-transformers with the all-MiniLM-L6-v2 model, stores them in ChromaDB
with source metadata attached to each chunk, and exposes a retrieve(query, k=5)
function. I will verify by running 3 of my 5 evaluation questions and checking that
the returned chunks are visibly relevant to each question and have distance scores
below 0.5.

**Milestone 5 — Generation and interface:**
I will give Claude my full planning.md and the grounding requirement from the
milestone instructions and ask it to implement a generate.py script that calls
retrieve() to get the top-5 chunks, passes them as context to Groq's
llama-3.3-70b-versatile model with a system prompt that instructs it to answer only
from the provided context, and returns the answer with source attribution. I will also
ask Claude to implement a Gradio web UI in app.py that accepts a question and displays
the answer and sources. I will verify by checking that responses cite specific source
documents and that asking an out-of-scope question produces an "I don't have enough
information" response rather than a hallucinated answer.