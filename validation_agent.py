from agno.agent import Agent
from agno.models.google import Gemini


validation_agent = Agent(
    model=Gemini(id="gemini-2.0-flash"),
    instructions=[
        "You are a validation agent. Your job is to validate the contents of the attached file.",
        "You will be provided with a file and you need to validate its contents.",
        "If the file is not valid, please provide a detailed explanation of why it is not valid.",
        "If the file is valid, please confirm that it is valid.",
    ]
    markdown=True,
    add_history_to_messages=True,
)