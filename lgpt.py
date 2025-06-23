import sys
from argparse import ArgumentParser
from query_process import process_query
from utils import typewriter, thinking_effect
import threading

# Setup thinking animation
stop_event = threading.Event()
thinking_thread = threading.Thread(
    target=thinking_effect, kwargs={"stop_event": stop_event}
)

def parse_args():
    response = None

    try:
        thinking_thread.start()
        parser = ArgumentParser(
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
            "prompt",
            type=str,
            nargs='*',
            help="The prompt to send to the model."
        )
        
        
        parser.add_argument(
            "-u","--update",
            type=str,
            help="Update Lgpt to latest version."
        )

        args = parser.parse_args()
        model = args.model
        update = parser.update
        
        if update:
            # call update funciton
            ...
        elif not sys.stdin.isatty():
            prompt = sys.stdin.read().strip()
        else:
            prompt = " ".join(args.prompt)

        response = process_query(prompt, model)

    except (KeyboardInterrupt, EOFError):
        response = "Process interrupted by user. Exiting..."
    except Exception as e:
        response = f"An error occurred: {e}"
    finally:
        stop_event.set()
        thinking_thread.join()

    return typewriter(response)

if __name__ == "__main__":
    parse_args()


# https://ko-fi.com/amiandev#
