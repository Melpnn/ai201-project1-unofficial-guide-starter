import chromadb
from sentence_transformers import SentenceTransformer
from ingest import load_documents, chunk_documents

COLLECTION_NAME = "scu_professors"

def embed_and_store():
    print("Loading and chunking documents...")
    documents = load_documents()
    chunks = chunk_documents(documents)

    print("Loading embedding model...")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    print("Setting up ChromaDB...")
    client = chromadb.PersistentClient(path="./chroma_db")
    
    try:
        client.delete_collection(COLLECTION_NAME)
    except:
        pass
    
    collection = client.create_collection(COLLECTION_NAME)

    print("Embedding chunks and storing in ChromaDB...")
    texts = [chunk["text"] for chunk in chunks]
    sources = [chunk["source"] for chunk in chunks]
    ids = [f"chunk_{i}" for i in range(len(chunks))]

    embeddings = model.encode(texts, show_progress_bar=True)

    collection.add(
        documents=texts,
        embeddings=embeddings.tolist(),
        metadatas=[{"source": s, "chunk_index": chunk["chunk_index"]} for s, chunk in zip(sources, chunks)],
        ids=ids
    )

    print(f"Done! Stored {len(chunks)} chunks in ChromaDB.")

def retrieve(query, k=5):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_collection(COLLECTION_NAME)

    query_embedding = model.encode([query]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=k
    )

    chunks = []
    for i in range(len(results["documents"][0])):
        chunks.append({
            "text": results["documents"][0][i],
            "source": results["metadatas"][0][i]["source"],
            "distance": results["distances"][0][i]
        })

    return chunks

if __name__ == "__main__":
    embed_and_store()

    print("\n--- RETRIEVAL TEST ---\n")
    test_queries = [
        "Is Natalie Linnell a tough grader?",
        "Which SCU CS professor do students recommend more, Tran or Linnell?",
        "Is Robert Finocchio's Business class worth taking?"
    ]

    for query in test_queries:
        print(f"Query: {query}")
        results = retrieve(query)
        for r in results:
            print(f"  Source: {r['source']} | Distance: {r['distance']:.3f}")
            print(f"  {r['text'][:150]}")
            print()
        print("-" * 50)