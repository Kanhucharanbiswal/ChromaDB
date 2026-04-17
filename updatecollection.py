import chromadb

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection("vehicles")

#update an existing document
collection.update(
    ids=["bus1"],
    documents=["Bus carries more than 40 passengers and runs on roads"]
)

print("update record for bus1")

record = collection.get(ids=["bus1"])
print(record)