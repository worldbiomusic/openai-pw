# openai-pw
Unofficial python wrapper of [OpenAI](https://openai.com/) API.

# Features
- Wrapped models (chat, audio, image, embeddings ...)
- History management

# Quick start
You can also play with in [this colab](https://colab.research.google.com/drive/1nJ1-YwLMSxSVx092uBVoarvuVUyt65xC?usp=drive_link). Or

1. Download `openai` and [`opaw`](https://pypi.org/project/opaw/) using pip. 
```cmd
pip install openai opaw
```
2. Create a `open-api-key.txt` file and insert your [api key](https://platform.openai.com/account/api-keys) into the file.
3. Write a demo code and play with ChatGPT.
```py
from opaw.examples.basic import loop_chat 
from opaw import util

util.setup() # api key setup
loop_chat() # start chat
```


# OpenAI
- [API](https://platform.openai.com/docs/api-reference/introduction)
- [model list](https://platform.openai.com/docs/models)
- [community](https://community.openai.com/)
- [usage](https://platform.openai.com/account/usage)
- [api key](https://platform.openai.com/account/api-keys)


# License
MIT