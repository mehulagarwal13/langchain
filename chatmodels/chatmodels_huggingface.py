from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint #yeh jab api use kar rha 
from dotenv import load_dotenv

load_dotenv()
llm=HuggingFaceEndpoint(repo_id="",task="text-generation")
model =ChatHuggingFace(llm=llm)
result=model.invoke("what is world famous dish")
print(result.content)
