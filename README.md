# openai-pw
Unofficial python wrapper of [OpenAI](https://openai.com/) API.

# Features
- Wrapped models (chat, audio, image, embeddings ...)
- 

# Quick start
1. Download [`opaw`](https://pypi.org/project/opaw/) using pip.
```cmd
pip install opaw
```

2. Create a `open-api-key.txt` file and insert your [api key](https://platform.openai.com/account/api-keys) into the file.

3. Write demo code.
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