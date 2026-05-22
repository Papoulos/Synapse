import os
from dotenv import load_dotenv
from crewai import LLM

load_dotenv()

def get_llm():
    return LLM(
        model=f"openai/{os.getenv('MODEL_NAME', 'gemma-4')}",
        base_url=os.getenv("OPENAI_API_BASE"),
        api_key=os.getenv("OPENAI_API_KEY")
    )
