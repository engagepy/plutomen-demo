import os
from dotenv import load_dotenv
from agents import Agent, Runner
import asyncio

# Load environment variables from .env file
load_dotenv()
# Set the OpenAI API key
# Ensure you have the OpenAI API key set in your environment or .env file
# For example, you can set it like this:
# export OPENAI_API_KEY="sk-..."
# or in your .env file:
# OPENAI_API_KEY="sk-..."
# Make sure to replace "sk-..." with your actual OpenAI API key
# If you are using a .env file, make sure to create it in the same directory as this script
# and add the line above to it.

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

xr_agent = Agent(name="Assistant", instructions="You are a XR tech assistant")

threed_agent = Agent(name="Assistant", instructions="You are a 3D Configurator assistant")

training_agent = Agent(name="Assistant", instructions="You are a poetic assistant")

triage_agent = Agent(
    name="Triage Agent",
    instructions="You determine which agent to use based on the user's input question",
    handoffs=[xr_agent, threed_agent, training_agent],
)


async def main():
    result = await Runner.run(triage_agent, "Write Plutomen hackthon ideas for XR, 3D Configurator, and Training")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())