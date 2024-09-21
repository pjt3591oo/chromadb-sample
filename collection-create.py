import chromadb
chroma_client = chromadb.HttpClient(host="localhost", port=8000)
print(chroma_client.list_collections())

collection = chroma_client.create_collection(
    name="new_collection", 
    metadata={'hnsw:space': 'l2'} # l2, ip, cosine
)
print(chroma_client.list_collections())