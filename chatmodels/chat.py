from dotenv import load_dotenv

load_dotenv()

# from langchain.chat_models import init_chat_model

# model = init_chat_model("gpt-5.4")
# response = model.invoke("What is cricket?")
# print(response.content)


from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(model = "mistral-small-2506",temperature=0,max_tokens=20)
response = model.invoke("Write a poem on computer?")
print(response.content)

