import chromadb
chroma_client = chromadb.HttpClient(host="localhost", port=8000)
print(chroma_client.list_collections())

collection = chroma_client.delete_collection(name="new_collection")
print(chroma_client.list_collections())