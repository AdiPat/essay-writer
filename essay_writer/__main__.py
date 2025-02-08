import traceback
import argparse
import os
from dotenv import load_dotenv
from .essay_writer import EssayWriter
from .printer import Printer as printer


def print_banner():
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


def reprompt_api_key():
    """
    Re-prompt the user for the API key and store it.

    Returns:
        None
    """
    api_key = input("Please enter your OpenAI API key: ")
    store_api_key(api_key)


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
        "-h", "--help", action="store_true", help="Show this help message and exit"
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

    if args.help:
        parser.print_help()
        return

    if args.set_key:
        store_api_key(args.set_key)
    if args.re_prompt:
        reprompt_api_key()
    if args.topic:
        writer = EssayWriter()
        essay = writer.write_essay(topic=args.topic)
        printer.print_green_message(f"Generated essay: \n{essay} ✍️")
    elif not args.set_key and not args.re_prompt and not args.topic:
        parser.print_help()


if __name__ == "__main__":
    main()
