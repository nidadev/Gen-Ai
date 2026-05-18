from dotenv import load_dotenv

load_dotenv()

from langchain.chat_models import init_chat_model

model = init_chat_model("gpt-5.4")
response = model.invoke("Why do parrots talk?")
print(response.content)