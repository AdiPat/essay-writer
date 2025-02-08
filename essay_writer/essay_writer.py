from dotenv import load_dotenv


load_dotenv(override=True, dotenv_path=".env")


class EssayWriter:
    """
    The EssayWriter class is the main class of the essay-writer package.
    It is used to generate essays based on the given prompt.
    In the first version, we use a simple LLM call to generate the essay.
    The essay writing can be configured using the provided settings.
    """

    def __init__(self, keys=None):
        self.keys = keys or {}

    def write_essay(self, topic, format="text"):
        # Placeholder for the actual essay writing logic
        return f"Essay on {topic} in {format} format."
