"""
ollama_client.py

Centralized LLM interface for StudyMate AI.
All agents use this file to communicate with Ollama.
"""

from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage


class OllamaClient:
    """
    Wrapper around ChatOllama.
    """

    def __init__(
        self,
        model_name: str = "qwen3.5:9b",
        temperature: float = 0.3,
    ):

        self.llm = ChatOllama(
            model=model_name,
            temperature=temperature,
        )

    def generate(self, system_prompt: str, user_prompt: str) -> str:
        """
        Sends prompts to the LLM and returns the response.
        """

        try:

            response = self.llm.invoke(
                [
                    SystemMessage(content=system_prompt),
                    HumanMessage(content=user_prompt),
                ]
            )

            return response.content

        except Exception as e:
            raise RuntimeError(f"Ollama Error: {e}")