from opaw.model.finetune import FinetuneBot
from opaw import util
from opaw.examples import setup

# api key
setup()

# finetune create
bot = FinetuneBot()
response = bot.create("test_memo for finetune create", task="create", training_file="file-8rh2wHJBIqj2xiPibQqKX62B")
print("finetune create:", response)

# finetune list
response = bot.create("test_memo for finetune list", task="list")
print("finetune list:", response)

# save history if needed
bot.save_history("history/finetune-hist.json")