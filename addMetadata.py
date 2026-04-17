import chromadb

# Step 1: connect to persistent storage
client = chromadb.PersistentClient(path="./chroma_db")

# step 2: create or reuse the collection
collection = client.get_or_create_collection("vehicles")

#step 3: Add documents with metadata
collection.add(
documents=[
    "Plane flies in the sky",
    "Boat travels on the water",
    "Bus is public transport on road",
    "Bicycle runs without fuel"
],
    ids=["bus1", "plane1", "boat1", "bike1"],
    metadatas=[
        {"type":"publice_transport", "fuel":"diesel"},
        {"type":"air_transport", "fuel":"jet"},
        {"type":"water_transport", "fuel":"diesel"},
        {"type":"personal_transport", "fuel":"manual"}
    ]
)
print("Data with metadata added successfully!")