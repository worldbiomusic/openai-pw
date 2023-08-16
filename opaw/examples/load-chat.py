from opaw.util import log
import json
from opaw.model.chat import ChatBot
from opaw.examples import setup
from opaw import util

# api key
setup()

# logger
logger = log.get("load-chat", "logs/load-chat.log")

# chat
bot = ChatBot()
bot.load_msgs("history/chat-hist.json")  # load history

response = bot.create("Then, what products are made in there?")
logger.info(f"response: {bot._get_res_msg(response)}")

bot.save_history("history/load-chat-hist.json")  # save history
