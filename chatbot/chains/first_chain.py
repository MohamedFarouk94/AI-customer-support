import json
from langchain_core.runnables import RunnableLambda
from prompts.first_prompt import first_prompt
from memory.history import get_history
from models.groq import first_model
from verbosity.verbose import print_json


def prepare_first_question(question):
    print("\n[thinking] Preparing the question to get analyzed.")
    prompt = first_prompt.format(question=question, history=get_history())
    return prompt


def get_json_response(prompt):
    print("[thinking] Analyzing the question.")
    response = first_model.invoke(prompt).content
    print("[thinking] Getting the analysis.")
    return response


def parse_json_response(response):
    try:
        data = json.loads(response)
    except json.JSONDecodeError:
        print(f"[thinking] The analysis was not in JSON Format: {response[:200]}")
        data = {'irrelevant': 1}

    print_json(data)
    return data


question_preparer = RunnableLambda(prepare_first_question)
json_getter = RunnableLambda(get_json_response)
json_parser = RunnableLambda(parse_json_response)

first_chain = question_preparer | json_getter | json_parser
