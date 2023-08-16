from opaw.util import log
from opaw.model.chat import ChatBot
from opaw import util
from opaw.examples import setup

# api key
setup()

# logger
logger = log.get("chat", "logs/chat.log")

# chat
def chat(prompt, **kargs):
    response = bot.create(prompt, **kargs)
    res_msg = response["choices"][0]["message"]["content"]
    logger.info(f"response: {res_msg}")


bot = ChatBot()
bot.add_message("You are a helpful assistant.", role="system")

chat("What is openai?")
chat("Then, who made it?")

# if memory is 0, bot don't know previous conversation (see chat-history.json for detail)
chat("What models are made in there?", memory=0)

# save history if needed
bot.save_history("history/chat-hist.json")
