import openai
from opaw.model.bot import Bot

class CompletionBot(Bot):
    """
    https://platform.openai.com/docs/api-reference/completions
    """
    def __init__(self, model="text-davinci-003"):
        super().__init__(model, "completion")

    def create(self, prompt, **kargs):
        if prompt is None:
            return None

        kargs["prompt"] = prompt
        request = {
            "model": self.model,
            **kargs
        }

        self._history_req(kargs)
        response = openai.Completion.create(**request)
        self._history_res(response)
        return response

