from langchain_core.messages import HumanMessage
from model import model

def chat():
    res = model.invoke([HumanMessage(content="Hi! I'm Srija.")])
    print(res)


if __name__ == "__main__":
    chat()
