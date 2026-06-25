import os
from langchain_text_splitters import RecursiveCharacterTextSplitter

DATA_FOLDER = "data"

def load_documents():
    documents = []
    for filename in os.listdir(DATA_FOLDER):
        if filename.endswith(".txt"):
            filepath = os.path.join(DATA_FOLDER, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()
            documents.append({
                "source": filename,
                "text": text
            })
    print(f"Loaded {len(documents)} documents")
    return documents

def clean_text(text):
    import re

    # fix HTML entities
    text = text.replace('&amp;', '&')
    text = text.replace('&nbsp;', ' ')
    text = text.replace('&#39;', "'")

    # remove leftover HTML tags
    text = re.sub(r'<[^>]+>', '', text)

    # collapse all whitespace to single space first
    text = re.sub(r'\s+', ' ', text)

    # remove metadata lines with colons (For Credit: Yes, Grade: A, etc.)
    text = re.sub(r'For Credit: \w+', '', text)
    text = re.sub(r'Attendance: [\w ]+?(?= Would| For|[A-Z][a-z])', '', text)
    text = re.sub(r'Would Take Again: \w+', '', text)
    text = re.sub(r'Grade: [\w\s+\-]+?(?=Textbook|For Credit|[A-Z][a-z]|$)', '', text)
    text = re.sub(r'Textbook: [\w/]+', '', text)

    # remove rating numbers and scores
    text = re.sub(r'\d+\.?\d* / 5', '', text)
    text = re.sub(r'Quality \d+\.?\d* Difficulty \d+\.?\d*', '', text)
    text = re.sub(r'Overall Quality Based on \d+ ratings', '', text)
    text = re.sub(r'\d+% Would take again', '', text)
    text = re.sub(r'\d+\.?\d* Level of Difficulty', '', text)
    text = re.sub(r'Awesome \d+ Great \d+ Good \d+ OK \d+ Awful \d+', '', text)
    text = re.sub(r'Awesome \d+\s*\d* Great \d+\s*\d* Good \d+\s*\d* OK \d+\s*\d* Awful \d+\s*\d*', '', text)

    # remove RMP UI text
    text = re.sub(r'Rate Arrow Icon Compare', '', text)
    text = re.sub(r'Rate Compare', '', text)
    text = re.sub(r"I'm Professor \w+", '', text)
    text = re.sub(r'Rating Distribution', '', text)
    text = re.sub(r'Similar Professors[\s\S]*?Student Ratings', '', text)
    text = re.sub(r'\d+ Student Ratings', '', text)
    text = re.sub(r'All courses', '', text)
    text = re.sub(r'Thumbs up \d+ Thumbs down \d+', '', text)
    text = re.sub(r'Reviewed', '', text)

    # remove professor reply blocks entirely
    text = re.sub(r'Professor \w+ says:.*?(?=Quality|For Credit|$)', '', text)
    text = re.sub(r'Posted on: .*?(?=Quality|For Credit|[A-Z][a-z]|$)', '', text)
    text = re.sub(r'Last Updated on: .*?(?=Quality|For Credit|[A-Z][a-z]|$)', '', text)

    # remove dates
    text = re.sub(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d+\w*, \d{4}', '', text)

    # remove course codes
    text = re.sub(r'\b(COEN|CSCI|BUSN|MGMT|CS|OMIS|FNCE|MKTG)\d+\w*\b', '', text)

    # remove professor/department header line
    text = re.sub(r'\w+ \w+ Professor in the [\w\s]+ department at Santa Clara University', '', text)
    text = re.sub(r'Professor in the [\w\s]+ department at Santa Clara University', '', text)

    # remove tag words
    tags = [
        'Tough grader', 'Lecture heavy', 'Test heavy', 'Lots of homework',
        'Participation matters', 'Group projects', 'Gives good feedback',
        'Clear grading criteria', 'Get ready to read', 'Amazing lectures',
        'Graded by few things', 'Accessible outside class', 'Hilarious',
        'Very professional', 'Caring', 'Helpful', 'Respected', 'Inspirational',
    ]
    for tag in tags:
        text = re.sub(tag, '', text, flags=re.IGNORECASE)

    # final whitespace cleanup
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()

    return text

def chunk_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50,
        length_function=len,
    )
    
    all_chunks = []
    for doc in documents:
        cleaned = clean_text(doc["text"])
        chunks = splitter.split_text(cleaned)
        for i, chunk in enumerate(chunks):
            if len(chunk) > 0:
                all_chunks.append({
                    "source": doc["source"],
                    "chunk_index": i,
                    "text": chunk
                })
    
    print(f"Total chunks: {len(all_chunks)}")
    return all_chunks

if __name__ == "__main__":
    documents = load_documents()
    chunks = chunk_documents(documents)
    
    print("\n--- 5 SAMPLE CHUNKS ---\n")
    for i, chunk in enumerate(chunks[:5]):
        print(f"Chunk {i+1} | Source: {chunk['source']}")
        print(chunk['text'])
        print("-" * 50)