import traceback
import sys
from dotenv import load_dotenv
from openai import OpenAI
from .printer import Printer as printer
from .utils import get_max_output_tokens

load_dotenv(override=True, dotenv_path=".env")


class EssayWriter:
    """
    The EssayWriter class is the main class of the essay-writer package.
    It is used to generate essays based on the given prompt.
    In the first version, we use a simple LLM call to generate the essay.
    The essay writing can be configured using the provided settings.
    """

    DEFAULT_OPENAI_MODEL = "gpt-4o-mini"
    DEFAULT_TEMPERATURE = 0.55

    def __init__(self, keys=None, model=DEFAULT_OPENAI_MODEL) -> None:
        """
        Initialize the EssayWriter class.

        Args:
            keys (dict): The API keys for the different services.

        Returns:
            None
        """
        self.keys = keys or {}

        if not self.validate_openai_key():
            sys.exit(1)

        self.model = model
        self.llm = self.init_llm()

    def validate_openai_key(self) -> bool:
        openai_api_key = self.keys.get("OPENAI_API_KEY")

        if openai_api_key is None:
            printer.print_red_message("OpenAI API key is not set. ❌")
            return False

        printer.print_green_message("OpenAI API key is set. ✅")
        return True

    def init_llm(self) -> OpenAI:
        """
        Initialize the OpenAI API.

        Returns:
            None
        """
        try:
            printer.print_green_message("Initializing LLM...    ")
            llm = OpenAI(api_key=self.keys.get("OPENAI_API_KEY"))
            printer.print_green_message("LLM initialized successfully.")
            return llm
        except Exception as e:
            printer.print_red_message(f"Error initializing LLM: {e} ❌")
            traceback.print_exc()
            sys.exit(1)

    def generate_error_response(self, topic: str, error: str, format: str) -> str:
        """
        Generate an error response for the given topic and error.

        Args:
            topic (str): The topic of the essay.
            error (str): The error message.
            format (str): The format of the essay.

        Returns:
            str: The error response.
        """
        markdown_error_response = f"""
                ### Error: {topic}
                Failed to generate essay due to an error.
                Error: {error}
            """
        text_error_response = f"""
                Failed to generate essay due to an error.
                Error: {error}
        """
        default_error_response = text_error_response
        if format == "markdown":
            return markdown_error_response
        elif format == "text":
            return text_error_response

        return default_error_response

    def write_essay(
        self, topic: str, format="markdown", temperature=DEFAULT_TEMPERATURE
    ) -> str:
        """
        Write an essay based on the given topic.

        Args:
            topic (str): The topic for the essay.
            format (str): The format of the essay (default: text).

        Returns:
            str: The generated essay.
        """
        try:
            printer.print_green_message(f"Writing essay on topic: {topic}...    ")

            system = """
                You are a helpful AI assistant called 'Essay Writer' that writes essays for students.
                You are a part of a Python package called 'essay-writer' that helps students generate essays on various topics.

                INSTRUCTIONS:
                - Given a topic, you will write an essay in the requested format.
                - Make sure the essay is well-structured and informative.
                - The essay should be factual, coherent, and well-researched.
                - Avoid hallucinations, plagiarism, and irrelevant content.
            """

            user_prompt = f"""
                Write an essay on the topic: '{topic}'
                Strictly Response in '{format}' format.
            """

            response = self.llm.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": system,
                    },
                    {"role": "user", "content": user_prompt},
                ],
                temperature=temperature,
                max_tokens=get_max_output_tokens(self.model),
            )
            printer.print_green_message(f"Essay written on '{topic}' successfully. 🎉")
            return response.choices[0].message.content
        except Exception as e:
            printer.print_red_message(f"Error writing essay: {e} ❌")
            traceback.print_exc()
            return self.generate_error_response(
                topic=topic, error=str(e), format=format
            )
