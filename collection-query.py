import chromadb
import time
from embedding import get_sentence_embedding

chroma_client = chromadb.HttpClient(host="localhost", port=8000)

collection = chroma_client.get_or_create_collection("new_collection")

results = collection.query(
    # query_texts=["This is a query document about florida"], # Chroma will embed this for you
    query_embeddings=[get_sentence_embedding("This is a query document about florida")], # Or you can embed it yourself
    n_results=1 # how many results to return
)

print(results)

results = collection.query(
    # query_texts=["This is a query document about florida"], # Chroma will embed this for you
    query_embeddings=[get_sentence_embedding("This is a query I'm JeongT")], # Or you can embed it yourself
    n_results=1 # how many results to return
)

print(results)