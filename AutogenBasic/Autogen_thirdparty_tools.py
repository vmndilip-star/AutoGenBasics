
import asyncio
from autogen.agentchat import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.tools import FunctionTool
from autogen_ext.tools.http import HttpTool
import os
from dotenv import load_dotenv
from langchain_community.utilities import GoogleSearchAPIWrapper
from autogen_ext.tools.http import HttpTool
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set")
model_client = OpenAIChatCompletionClient(model='gpt-4o', api_key=api_key)
