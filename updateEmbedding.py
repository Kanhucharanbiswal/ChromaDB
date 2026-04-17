import chromadb

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection("vehicles_embeddings")

# Step 1; update a record
collection.update(
    ids=["car1"],
    documents=["Car runs on electricity insted of petrole"]
)
print(" Document Updated!")

# Step 2: retrive new embedding
updated = collection.get(ids=["car1"], include=["documents", "embeddings"])
print(f" Update Text: {updated['documents'][0]}")
print(f" Updated Embedding (first 10 values): {updated['embeddings'][0][:10]}")