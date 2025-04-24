import os
from datetime import datetime


# A clean version of the chat hitory
# To be sent to the LLM
chat_history = []

# A version of chat history including welcoming message
# It's also incudeing all the messages even the irrelevant ones.
# Only used to save conversation
full_chat_history = []

N = 5  # max numbers of recent messages retrieved


def get_history():
    global chat_history
    return chat_history[-N:]


def update_history(user_input, response):
    global chat_history
    chat_history.append({"role": "user", "content": user_input})
    chat_history.append({"role": "assistant", "content": response})


def update_full_history(who, what):
    global full_chat_history
    full_chat_history.append(f"{who}: {what}")


def save_history():
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"chat{timestamp}.txt"
    filepath = os.path.join('memory/saved_conversations', filename)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(full_chat_history))
