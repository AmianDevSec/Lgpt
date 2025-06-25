import sys
from argparse import ArgumentParser
from query_process import process_query
from utils import typewriter, helper, error_string_styled
from lgpt_updater import stop_event, thinking_thread, lgpt_updater  

LGPT_VERSION = "1.2.0"

def lgpt() -> None:
    response = ""
    
    try:
        thinking_thread.start()
        parser = ArgumentParser(
            add_help=False,
            description="Lgpt: A command-line utility for managing and interacting with large language models (LLMs) from the Linux terminal."
        )

        parser.add_argument(
            "--model",
            type=str,
            choices=["perplexity", "gemini", "deepseek", "llama"],
            default='deepseek',
            help="The model to use for processing the query."
        )

        parser.add_argument(
            '-h', 
            '--help', 
            action='store_true', 
            help='Show help and exit')

        parser.add_argument(
            "prompt",
            type=str,
            nargs='*',
            help="The prompt to send to the model."
        )

        parser.add_argument(
            "-u",
            "--update",
            action="store_true",
            help="Update Lgpt to latest version."
        )

        parser.add_argument(
            "-v",
            "--version",
            action="store_true",
            help="Prints the current version of Lgpt.",
        )

        args = parser.parse_args()

        model = args.model
        update = args.update
        version = args.version
        help = args.help
        prompt = ""

        if update:
            return lgpt_updater()
        elif help:
            response = helper()
        elif version:
            response = LGPT_VERSION
        elif not sys.stdin.isatty():
            prompt = sys.stdin.read().strip()
        else:
            prompt = " ".join(args.prompt)

        response = process_query(prompt, model) if not bool(response) and bool(prompt) else response
        # isError = False
        
    except (KeyboardInterrupt, EOFError):
        response = error_string_styled("Process interrupted by user. Exiting...")
        # isError = True
    except Exception as e:
        response = error_string_styled(f"An error occurred: {e}")
        # isError = True
    finally:
        stop_event.set()
        thinking_thread.join()

    return typewriter(response)

if __name__ == "__main__":
    lgpt()
