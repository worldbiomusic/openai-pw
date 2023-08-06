from opaw.model.chat import ChatBot
from opaw import util
from opaw.examples import setup

# api key
setup()

# chat
def chat(prompt):
    response = bot.create(prompt)
    res_msg = response["choices"][0]["message"]["content"]
    print("response:", res_msg)


bot = ChatBot()
bot.add_message("You are a helpful assistant.", role="system")

chat("What is openai?")
chat("Then, who made it?")

# save history if needed
bot.save_history("history/chat-hist.json")
