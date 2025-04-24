from langchain_core.runnables import RunnableLambda
from prompts.final_prompt import final_prompt
from models.groq import final_model


def prepare_final_question(inputs):
    print("[thinking] Preparing the question to get answered.")
    question = inputs['rewritten-question']
    documents = inputs['documents']
    return final_prompt.format(question=question, documents=documents)


def get_final_answer(prompt):
    print("[thinking] Answering the question.")
    response = final_model.invoke(prompt)
    return response.content


question_preparer = RunnableLambda(prepare_final_question)
answer_getter = RunnableLambda(get_final_answer)

final_chain = question_preparer | answer_getter
