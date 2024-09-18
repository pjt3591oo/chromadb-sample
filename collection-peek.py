import chromadb
chroma_client = chromadb.HttpClient(host="localhost", port=8000)


collection = chroma_client.get_collection("new_collection")
print(collection.peek())

collection_count = chroma_client.count_collections()
print(chroma_client.list_collections())

print(collection_count)