import chromadb

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection("vehicles")

#Delete one document
collection.delete(ids=["boat1"])

#retrieve all stored data
data = collection.get()

print("remaining documents inside 'vehicles':")
for i, doc in zip(data["ids"], data["documents"]):
    print(f"{i} → {doc}")