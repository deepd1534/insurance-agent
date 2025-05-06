
from pathlib import Path
from time import sleep

from agno.agent import Agent
from agno.media import File
from agno.models.google import Gemini
from google import genai

pdf_path = Path(__file__).parent.joinpath("data/Claim1.pdf")

client = genai.Client()

# Upload the file to Google GenAI
upload_result = client.files.upload(file=pdf_path)

# Get the file from Google GenAI
retrieved_file = client.files.get(name=upload_result.name)

# Retry up to 3 times if file is not ready
retries = 0
wait_time = 5
while retrieved_file is None and retries < 3:
    retries += 1
    sleep(wait_time)
    retrieved_file = client.files.get(name=upload_result.name)

if retrieved_file is not None:
    agent = Agent(
        model=Gemini(id="gemini-2.0-flash"),
        markdown=True,
        add_history_to_messages=True,
    )

    agent.print_response(
        "Summarize the contents of the attached file.",
        files=[File(external=retrieved_file)],
    )

    agent.print_response(
        "What does this document say.",
    )
else:
    print("Error: File was not ready after multiple attempts.")