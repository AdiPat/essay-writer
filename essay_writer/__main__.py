import traceback
import argparse
import os
from dotenv import load_dotenv
from .essay_writer import EssayWriter
from .printer import Printer as printer


def print_banner():
    """
    Prints an aesthetically pleasing banner for the Essay Writer tool.
    Uses the Printer class from the printer module to print colored text.

    Args:
        None

    Returns:
        None
    """
    banner = """
    ✨ Welcome to Essay Writer ✨
    Your AI-powered essay generation tool.
    Developed by Aditya Patange (AdiPat) and Sarvesh Bhujle (SarveshBhujle).
    """
    printer.print_purple_message(banner)


def store_api_key(api_key):
    """
    Store the API key in a hidden folder at home.

    Args:
        api_key (str): The OpenAI API key to store.

    Returns:
        None
    """
    try:
        home = os.path.expanduser("~")
        config_dir = os.path.join(home, ".essay_writer")
        os.makedirs(config_dir, exist_ok=True)
        key_file = os.path.join(config_dir, "open_ai_api_key.txt")
        with open(key_file, "w") as f:
            f.write(api_key)
        printer.print_green_message(f"API key stored successfully in {key_file} 🎉")
    except Exception as e:
        printer.print_red_message(f"Error storing API key: {e} ❌")
        traceback.print_exc()


def get_api_key():
    """
    Retrieve the OpenAI API key from the file.

    Returns:
        str: The OpenAI API key.
    """
    try:
        home = os.path.expanduser("~")
        key_file = os.path.join(home, ".essay_writer", "open_ai_api_key.txt")
        with open(key_file, "r") as f:
            api_key = f.read().strip()
        return api_key
    except Exception as e:
        printer.print_red_message(f"Error retrieving API key: {e} ❌")
        traceback.print_exc()
        return None


def reprompt_api_key():
    """
    Re-prompt the user for the API key and store it.

    Args:
        None

    Returns:
        None
    """
    api_key = input("Please enter your OpenAI API key: ")
    store_api_key(api_key)


def check_and_prompt_api_key():
    """
    Check if the API key is set. If not, prompt the user to enter it.

    Args:
        None

    Returns:
        None
    """
    home = os.path.expanduser("~")
    key_file = os.path.join(home, ".essay_writer", "open_ai_api_key.txt")
    if not os.path.exists(key_file):
        printer.print_red_message(
            "API key not found. Please enter your OpenAI API key."
        )
        reprompt_api_key()


def generate_output_filename(title):
    """
    Generate an output filename based on the title.

    Args:
        title (str): The title of the essay.

    Returns:
        str: The generated filename.
    """
    filename = "".join(char if char.isalnum() else " " for char in title)
    filename = "_".join(filename.split())
    filename = filename.lower()
    return f"{filename}.md"


def init_parser():
    """
    Initialize the argument parser.

    Returns:
        argparse.ArgumentParser: The initialized argument parser.
    """
    parser = argparse.ArgumentParser(description="Essay Writer CLI")
    parser.add_argument("--topic", type=str, help="The topic for the essay")
    parser.add_argument("--set-key", type=str, help="Set the OpenAI API key")
    parser.add_argument(
        "-r", "--re-prompt", action="store_true", help="Re-prompt for the API key"
    )
    parser.add_argument(
        "--format",
        type=str,
        choices=["markdown", "plain-text"],
        default="markdown",
        help="The format of the output file (default: markdown)",
    )
    return parser


def main():
    """
    The main function of the essay-writer package.

    This function is the entry point for the essay-writer package. It is called when the package is run as a script.

    Args:
        None

    Returns:
        None
    """
    print_banner()
    try:
        load_dotenv(override=True, dotenv_path=".env")
    except Exception as e:
        printer.print_red_message(f"Error loading .env file: {e} ❌")
        traceback.print_exc()

    parser = init_parser()
    args = parser.parse_args()

    check_and_prompt_api_key()

    api_key = get_api_key()
    if not api_key:
        printer.print_red_message("Failed to retrieve API key. Exiting... ❌")
        return

    if args.set_key:
        store_api_key(args.set_key)
    if args.re_prompt:
        reprompt_api_key()
    if args.topic:
        writer = EssayWriter(keys={"OPENAI_API_KEY": api_key})
        essay = writer.write_essay(topic=args.topic, format=args.format)
        output_filename = generate_output_filename(args.topic)
        if args.format == "plain-text":
            output_filename = output_filename.replace(".md", ".txt")
        with open(output_filename, "w") as f:
            f.write(essay)
        printer.print_green_message(f"Generated essay saved to {output_filename} ✍️")
    elif not args.set_key and not args.re_prompt and not args.topic:
        parser.print_help()


if __name__ == "__main__":
    main()
