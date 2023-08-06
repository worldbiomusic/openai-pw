import copy
import io
from opaw import tool
import json
import opaw.tool
import openai
from opaw.model import bot
from opaw import util


class ChatBot(bot.Bot):
    """
    https://platform.openai.com/docs/api-reference/chat
    """

    def __init__(self, model="gpt-3.5-turbo", messages=None):
        super().__init__(model, "chat")
        # conversations
        self.messages = [] if messages is None else messages

    def create(self, content=None, **kargs):
        """
        Gets a response from bot
        :param content: get a response with messages (content)
        :param kargs: other args
        :return:
        """
        # default
        role = kargs["role"] if kargs.get("role") else "user"

        if content is not None:
            content = str(content)
            self.add_message(content, role=role)

        request = {
            "model": self.model,
            "messages": self.messages,
            **kargs
        }

        self._history_req(request)

        response = openai.ChatCompletion.create(**request)

        # insert response message to the messages
        res_msg = self._get_res_msg(response)
        self.messages.append(res_msg)
        self._history_res(response)

        return response

    def add_message(self, content, role="user"):
        self.messages.append({"role": role, "content": content})

    def call_function(self, response):
        fn_call = self.get_fn_call(response)

        # if function_call exist
        if fn_call:
            function_name = fn_call["name"]
            function = tool.functions[function_name]

            fn_args = json.loads(fn_call["arguments"])
            return function(**fn_args)

    def get_fn_call(self, response):
        return self._get_res_msg(response).get("function_call")

    def _get_res_msg(self, response):
        return response["choices"][0]["message"]

    def total_tokens(self, messages):
        """
        returns number of used all tokens
        """
        return sum([int(msg["usage"]["total_tokens"]) for msg in messages])

    def load_msgs(self, history):
        """
        loads conversation history
        :param history: type could be a file or file path or dict
        """

        if isinstance(history, str):  # file path (str)
            with open(history) as f:
                hist = json.load(f)
        elif isinstance(history, io.IOBase):  # file
            hist = json.load(history)
        elif isinstance(history, dict):  # json dict
            hist = history
        else:
            return

        # load history
        self.history = copy.deepcopy(hist)

        # load messages of the last request
        self.messages = next((item["messages"] for item in hist[::-1] if "messages" in item), [])

        # insert last response to messages
        last_res_msg = next((self._get_res_msg(item) for item in hist[::-1] if "choices" in item), None)
        self.messages.append(last_res_msg)
