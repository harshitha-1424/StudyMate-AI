from ollama_client import OllamaClient

client = OllamaClient()

response = client.generate(
    system_prompt="You are a helpful AI mentor.",
    user_prompt="Introduce yourself in two lines."
)

print(response)