import chromadb
import uuid
from embedding import get_sentence_embedding

chroma_client = chromadb.HttpClient(host="localhost", port=8000)

collection = chroma_client.get_or_create_collection("new_collection", embedding_function=get_sentence_embedding)

documents=[
    "This is a document about pineapple",
    "This is a document about oranges",
    "This is a document about apples",
    "I'm JeongTae Park"
]

# embeddings = [
#     get_sentence_embedding(document) for document in documents
# ]

ids = [
    str(uuid.uuid4()) for i in range(len(documents))
]

metadatas = [
    {"index": i, "version": 1.0} for i in range(len(documents))
]

collection.add(
    documents=documents,
    # embeddings=embeddings,
    metadatas=metadatas,
    ids = ids
)
