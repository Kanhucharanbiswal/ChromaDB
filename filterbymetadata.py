import chromadb

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection("vehicles")

# Example 1: Filter by transport type
public_transport = collection.get(where={"type": "public_transport"} )
print("Public Transport:")
print(public_transport)

# Example 1: Filter by fuel type type
diesel_vehicles = collection.get(where={"fuel": "diesel"})
print("\n Diesel Vehicles:")
print(diesel_vehicles)