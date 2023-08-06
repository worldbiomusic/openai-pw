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

    def create(self, prompt=None, **kargs):
        """
        Gets a response from bot
        :param prompt: get a response with messages (content)
        :param kargs: other args
        :return:
        """
        # default
        role = kargs["role"] if kargs.get("role") else "user"

        if prompt is not None:
            prompt = str(prompt)
            self.messages.append({"role": role, "content": prompt})

        # kargs["msg"] = self.messages[-1]
        request = {
            "model": self.model,
            "messages": self.messages,
            **kargs
        }

        self._history_req(kargs)
        # kargs.pop("msg", None)  # remove prompt key after history saved

        response = openai.ChatCompletion.create(**request)

        # insert response message to the messages
        res_msg = self._get_res_msg(response)
        self.messages.append(res_msg)
        self._history_res(response)

        return response

    def add_message(self, content, role="user"):
        self.messages.append({"role": role, "content": content})
        self._history_req(self.messages[-1])

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

    def load_msgs(self, msgs):
        """
        loads conversation history
        :param msgs: type could be a file or file path or dict

        ['created', 'from', 'model', 'prompt', 'type']

        """

        if isinstance(msgs, str):  # file path (str)
            with open(msgs) as f:
                messages = json.load(f)
        elif isinstance(msgs, io.IOBase):  # file
            messages = json.load(msgs)
        elif isinstance(msgs, dict):  # json dict
            messages = msgs
        else:
            return

        self.messages = util.filter_args(messages)


