import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()


GROQ_API_KEY = os.getenv("GROQ_API_KEY")
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

first_model = ChatGroq(temperature=0, model_name="llama-3.1-8b-instant")
final_model = ChatGroq(temperature=0, model_name="llama-3.1-8b-instant")

# Yes, they're the same
# But I kept the logic open to the possibility of using two different models
