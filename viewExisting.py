import chromadb

# Connect to the same persistent storage
client = chromadb.PersistentClient(path="./chroma_db")

#Get the existing collection
collection = client.get_collection("vehicles")

#Retrieve all stored data
data = collection.get()

print(" All documents inside 'vehicles' : ")
for i, doc in zip(data["ids"], data["documents"]):
    print(f"{i} → {doc}")