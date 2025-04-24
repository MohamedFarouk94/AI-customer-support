chat_history = []


def get_history():
    global chat_history
    return chat_history[-5:]


def update_history(user_input, response):
    global chat_history
    chat_history.append({"role": "user", "content": user_input})
    chat_history.append({"role": "assistant", "content": response})
