from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

PROMPTS_DIR = BASE_DIR / "prompts"


def load_prompt(prompt_name: str) -> str:

    prompt_path = PROMPTS_DIR / prompt_name

    if not prompt_path.exists():
        raise FileNotFoundError(
            f"Prompt file '{prompt_name}' not found at {prompt_path}"
        )

    with open(prompt_path, "r", encoding="utf-8") as file:
        return file.read()
