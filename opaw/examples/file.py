from opaw.model.file import FileBot
from opaw import util
from opaw.examples import setup

# api key
setup()

bot = FileBot()

# file upload
response = bot.create(task="upload", file="file-upload.jsonl", purpose="fine-tune")
print("file-upload response:", response)
id = response["id"]

# retrieve a file
response = bot.create(task="retrieve", id=id)
print("list response:", response)

# download file
response = bot.create(task="download", id=id)
print("download response:", response)
print(type(response))

# save history if needed
bot.save_history("history/file-hist.json")

