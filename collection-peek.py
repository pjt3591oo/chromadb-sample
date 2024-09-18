import chromadb
chroma_client = chromadb.HttpClient(host="localhost", port=8000)
print(chroma_client.list_collections())

collection = chroma_client.get_collection("new_collection")
print(collection.peek())