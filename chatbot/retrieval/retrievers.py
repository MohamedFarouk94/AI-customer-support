from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
import warnings
from langchain_core._api.deprecation import LangChainDeprecationWarning

warnings.filterwarnings("ignore", category=LangChainDeprecationWarning)


embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

product_retriever = Chroma(
    collection_name="products",
    embedding_function=embedding_model,
    persist_directory="vectorstores/chroma_products"
).as_retriever(search_kwargs={"k": 6})

policy_retriever = Chroma(
    collection_name="policy",
    embedding_function=embedding_model,
    persist_directory="vectorstores/chroma_policy"
).as_retriever(search_kwargs={"k": 4})
