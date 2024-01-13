import asyncio
from rasa.core.agent import Agent
path = 'models/20240112-191517-charcoal-log.tar'
class Model:

    def __init__(self, model_path: str) -> None:
        self.agent = Agent.load(path)
        print("NLU model loaded")


    def message(self, message: str) -> str:
        message = message.strip()
        return asyncio.run(self.agent.parse_message(message))

mdl = Model(path)
sentence = "Can i get more info about your website?"
print(mdl.message(sentence))