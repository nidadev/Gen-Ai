from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name = "ibm-granite/granite-embedding-97m-multilingual-r2"
)
texts = [
    'what are you doing?'
    'hello this is github'
]

vector = embeddings.embed_documents(texts)
print(vector)