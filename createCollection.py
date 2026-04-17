import chromadb

#Connect to chroma with persistence
client = chromadb.PersistentClient(path="./chroma_db")

# Create or reuse a collection
collection = client.get_or_create_collection(name="vehicles")

print("Collection ready:", collection.name)

# Add some sample records
collection.add(
documents=[
    "Car runs on land",
    "Plane flies in the sky",
    "Boat travels on the water",
    "Bus is public transport on road",
],
ids=["car1", "plane1", "boat1", "bus1"]
)

print(" Sample data added successfully!")

data = collection.get()
print(" Current data:")
for i, doc in zip(data["ids"], data["documents"]):
    print(f"{i} → {doc}")