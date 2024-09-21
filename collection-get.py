import chromadb

chroma_client = chromadb.HttpClient(host="localhost", port=8000)

collection = chroma_client.get_or_create_collection("new_collection")

results = collection.get(
    where_document={
        "$contains": "about"
    },
    where={
        "index": {
            "$gt": 1
        }
    },
    # ids=[]
)

print(results)

