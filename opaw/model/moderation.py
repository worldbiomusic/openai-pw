import openai
from opaw.model.bot import Bot


class ModerationBot(Bot):
    """
    https://platform.openai.com/docs/api-reference/moderations
    """

    def __init__(self, model="text-moderation-latest"):
        super().__init__(model, "moderation")

    def create(self, prompt, **kargs):
        input = prompt
        if input is None:
            return None

        kargs["input"] = input
        request = {
            "model": self.model,
            **kargs
        }

        self._history_req(kargs)
        response = openai.Moderation.create(**request)
        self._history_res(response)
        return response
