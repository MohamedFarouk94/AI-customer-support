
# AI Customer Support

This is an AI-powered customer support system designed to assist users through a CLI. The project uses RAG (Retrieval-Augmented Generation) architecture, with LangChain, HuggingFaceEmbeddings, and GroqCloud API.

---

## 🚀 How to Install and Run

Follow the steps below to set up and run the application on your local machine.


### 1. Create a Virtual Environment

Inside the root folder, create a python virtual environment.
```bash
python3 -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
```

### 2. Install Dependencies
Run the following bash code in the root directory.

```bash
pip install -r requirements.txt
```

### 4. Prepare Vector Stores

Run the data preprocessing steps using the Jupyter notebook:

```bash
jupyter notebook data-handling/data_handling.ipynb
```


- The notebook will prepare the data and create vectorstores for products and policy.
- An HTML version `data-handling/data_handling.html` is there for the sake of easy reading.

### 5. Run the Chatbot
Run these bash lines in the root directory.
```bash
cd chatbot
python main.py
```
### 6. Chat!
You will see something like that. 
```
ASSISTANT: Hi! I'm here to help you in anything related to our products and policy. How can I help you?

[help] Type 'exit' without quotations to end the conversation.
[help] Type 'exit-save' without quotations to end the conversation.


YOU:
```
- Now you can use this CLI to communicate with our assistant.
- When you type your question and click `enter` you will see the thinking steps before the response is displayed, the thinking steps will be something like this:
```
[thinking] Preparing the question to get analyzed.
[thinking] Analyzing the question.
[thinking] Getting the analysis.
[thinking] Enhanced version of the question: Do you sell USB products?
[thinking] Keywords for related products docs: usb
[thinking] The question does not need policy data.
[thinking] Getting relevant documents from products data.
[thinking] Found 6 relative products data.
[thinking] Preparing the question to get answered.
[thinking] Answering the question.

```
- When typing `exit-save` the conversation will be stored as a txt file in `chatbot/memory/saved_conversation`.
---
## 📌 Examples
- Examples can be found in form of videos and txt files in `exampls` folder.

## 🧠 Approach Explanation

### `main.py`

- As you may have noticed, this is the main file that is actually run when you run chatbot.
- This is just the loop that runs the bot.
- It completely deplends on the function `ask_and_answer` from `ask.py` file. 

### `ask.py`

- This file contains the most important function `ask_and_answer` which implements the whole procedure for only one question.
- It takes the user question and runs it through three chains: `first_chain`, `middle_chain` and `final_chain`.
- `first_chain` is responsible for analyzing the question and enhancing it using the LLM. If the question turned to be irrelevant or abuse/misuse the procedure halts immediatley and a "sorry I cannot response..." message will be displayed.
- `middle_chain` is responsible for retrieving data from the vector stores that's related to the user's question.
- `final_chain` is responsible for sending the enhanced question along with the relevant data to the LLM in order to get answered.

<p align="center">
  <img src="https://i.imgur.com/8KIQDKI.jpeg" alt="Chains Infograph" width="250"/>
</p>


### `chains/first_chain.py`
- The first chain takes the user's question along with chat history and asks the LLM to create a JSON object containing the question metadata in the following form:
```json
{
"rewritten-question": "...", # enhanced version of the question with the context of chat history
"products-keywords": "...",  # keywords to search in keywords data, empty if no needed
"policy-keywords": "...",    # keywords to search in policy data, empty if no needed
"irrelevant": 0,             # 1 if the question is misuse/abuse/irrelevant, otherwise 0
}
```
### `chains/middle_chain.py`
- The middle chain is responsible for retrieving data using the keywords generated in the question metadata through the first chain.
### `chains/final_chain.py`
- The final chain is the last step where the LLM takes the enhanced question and the related retrieved data and gives the response which is to be displayed in the user's screen.
### `Other folders`
- `memory` contains `history.py` file, which has the logic of updating, getting and saving chat history.
- `models` contains `groq.py` file, which contains the api calling process, and has two models: `first_model` and `final_model` to be used in the first and final chain respectively. Currently, they're the same model, but the logic is open to use two different models if needed.
- `prompts` contains `first_prompt.py` and `final_prompt.py` which contain the prompts used in the first and final chains respectively.
- `retrieval` contains `retrievers.py` file which has both the products and the policy data retrievers.
- `vectorstores` where ChromaDB files live as they created via the Jupyter notebook.
- `verbosity` contains `verbose.py` which has functions that display the JSON object content, and the \[help\] messages.
- `examples` contains three examples each one in form of video and txt file. 
---

## 🔮 Future Work / Possible Enhancements
1. Migrating from ChromaDB to ElasticSearch so both semantic queries and filtering could be handled (e.g.:Recommend a laptop under $800.)
2. Deploying with Django, Flask or Fast API, and creating a front-end to run the program on browser.
3. As an alternative to option #2, creating a GUI using tkinter or any similar Python library.



