from chains.first_chain import first_chain
from chains.middle_chain import middle_chain
from chains.final_chain import final_chain
from memory.history import update_history, update_full_history


sorry_response = "Sorry I cannot answer your question. I'm an AI customer-assistant and can help you in anything related to our products and/or policy."
middle_and_final_chain = middle_chain | final_chain


def ask_and_answer(question):
    response = first_chain.invoke(question)

    if response['irrelevant']:
        update_full_history("YOU", question)
        update_full_history("ASSISTANT", sorry_response)
        return sorry_response

    answer = middle_and_final_chain.invoke(response)
    update_history(question, answer)
    update_full_history("YOU", question)
    update_full_history("ASSISTANT", answer)
    return answer
