import os
from dotenv import load_dotenv
from groq import Groq
from embed import retrieve

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask(question):
    chunks = retrieve(question, k=5)
    
    context = ""
    sources = []
    for chunk in chunks:
        context += f"Source: {chunk['source']}\n{chunk['text']}\n\n"
        if chunk['source'] not in sources:
            sources.append(chunk['source'])
    
    system_prompt = """You are a helpful assistant that answers questions about SCU 
professors and courses using ONLY the student reviews provided to you.

STRICT RULES:
- Answer ONLY using information from the provided documents
- Do NOT use any outside knowledge or general assumptions about professors
- If the documents do not contain enough information to answer the question, 
  say exactly: "I don't have enough information in my documents to answer that."
- Always refer to specific things students said in the reviews
- Never make up or infer information that isn't explicitly in the documents"""

    user_prompt = f"""Here are the relevant student reviews:

{context}

Question: {question}

Answer using only the reviews above. Be specific and cite what students said."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.2
    )

    answer = response.choices[0].message.content

    return {
        "answer": answer,
        "sources": sources
    }