import chromadb
client = chromadb.Client()

collection = client.create_collection(name="vehicles")

print("collection created : ", collection.name)

#Add Data to collection
collection.add(
documents=[
    "Car runs on land",
    "Plane flies in the sky",
    "Boat travels on the water",
    "Bus is public transport on road"
],
ids=["car1", "plane1", "boat1", "bus1"]
)

#query the Collection
results = collection.query(
query_texts=["vehicle that run on the road"],
n_results = 2
)

#print the output
print(results)