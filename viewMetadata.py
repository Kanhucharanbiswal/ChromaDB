import chromadb

# Step 1: Connect to chroma
client = chromadb.PersistentClient(path="./chroma_db")

# Step 2: Access the collection
collection = client.get_collection("vehicles")

# Step 3: Retrieve documents with metadata
data = collection.get(include=[ "documents", "metadatas"])

print("All documents with metadata:")
for i, doc, meta in zip(data["ids"], data["documents"], data["metadatas"]):
    print(f"{i} → {doc} | Metadata: {meta}")