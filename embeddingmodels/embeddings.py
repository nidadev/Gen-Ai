from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
embeddings = OpenAIEmbeddings(
    model = "text-embedding-3-small",
    dimensions=64
)
texts = [
    'what are you doing?'
    'hello this is github'
]

vector = embeddings.embed_documents(texts)
#vector = embeddings.embed_query("write a script on grandfather")

print(vector)