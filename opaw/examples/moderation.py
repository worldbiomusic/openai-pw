from opaw.model.moderation import ModerationBot
from opaw import util
from opaw.examples import setup

# api key
setup()

# moderation
bot = ModerationBot()
prompt = "I want to kill them!!"
response = bot.create(prompt)
print(response)
result = response["results"][0]
flagged = result["flagged"]
categories = result["categories"]
scores = result["category_scores"]
true_flags = {flag: scores[flag] for flag, value in categories.items() if value}

print("flagged:", flagged)
print("flags:", true_flags)

# save history if needed
bot.save_history("history/moderation-hist.json")
