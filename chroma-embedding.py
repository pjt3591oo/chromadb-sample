import chromadb
import uuid
from chromadb.utils import embedding_functions

model_name = "Huffon/sentence-klue-roberta-base"
default_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=model_name)

rst = default_ef(["This is a document about pineapple"])

chroma_client = chromadb.HttpClient(host="localhost", port=8000)

collection = chroma_client.get_or_create_collection("new_collection", embedding_function=default_ef)

documents=[
    "This is a document about pineapple",
    "This is a document about oranges",
    "This is a document about apples",
    "I'm JeongTae Park"
]

ids = [
    str(uuid.uuid4()) for i in range(len(documents))
]

metadatas = [
    {"index": i, "version": 1.0} for i in range(len(documents))
]

collection.add(
    documents=documents,
    metadatas=metadatas,
    ids = ids
)