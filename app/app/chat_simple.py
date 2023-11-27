from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.9, max_tokens=100)

message = [
    HumanMessage(content="Hello, how are you?"),
]

result = chat(message)

print(result)
