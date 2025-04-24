from langchain_core.runnables import RunnableLambda
from retrieval.retrievers import product_retriever, policy_retriever


def retrieve_documents(inputs):
    docs = []
    products_keywords = inputs['products-keywords']
    policy_keywords = inputs['policy-keywords']

    if products_keywords:
        print("[thinking] Getting relevant documents from products data.")
        products_docs = product_retriever.invoke(products_keywords)
        print(f"[thinking] Found {len(products_docs)} relative products data.")
        docs += products_docs

    if policy_keywords:
        print("[thinking] Getting relevant documents from policy data.")
        policy_docs = policy_retriever.invoke(policy_keywords)
        print(f"[thinking] Found {len(policy_docs)} relative policy data.")
        docs += policy_docs

    inputs['documents'] = docs
    return inputs


middle_chain = RunnableLambda(retrieve_documents)
