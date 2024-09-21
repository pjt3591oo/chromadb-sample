from chromadb.api.types import (
    Documents,
    EmbeddingFunction,
    Embeddings,
)
from transformers import AutoTokenizer, AutoModel
import torch.nn.functional as F
import torch


class MySentenceEmbedding(EmbeddingFunction[Documents]):

    def __init__(
        self,
        model_id: str = "distilbert-base-uncased",
    ):
        self.model_id = model_id
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        self.model = AutoModel.from_pretrained(model_id)
    
    def __call__(self, documents: Documents) -> Embeddings:
        embeddings = []
        for document in documents:
            text = document
            encoded_input = self.tokenizer(text, padding=True, truncation=True, return_tensors='pt')

            with torch.no_grad():
                model_output = self.model(**encoded_input)

            sentence_embeddings = self._mean_pooling(model_output, encoded_input['attention_mask'])

            sentence_embeddings = F.normalize(sentence_embeddings, p=2, dim=1)

            embeddings.append(sentence_embeddings.tolist()[0])
        
        return embeddings
    
    @classmethod
    def _mean_pooling(cls, model_output, attention_mask):
        token_embeddings = model_output[0] #First element of model_output contains all token embeddings
        input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
        return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)


get_sentence_embedding = MySentenceEmbedding()


if __name__ == '__main__':
    
    rst = get_sentence_embedding(["Love is wanting to be loved"])
    print(rst)