from opaw.model.audio import AudioBot
from opaw import util
from opaw.examples import setup

# api key
setup()

# audio
bot = AudioBot()

# transcript (language: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)
response = bot.create("audio1.mp3", task="stt", language="en")
print("stt:", response["text"])

# translation
response = bot.create("audio1.mp3", task="mt", language="en")
print("mt:", response["text"])

# save history if needed
bot.save_history("history/audio-hist.json")

