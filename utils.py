import time
import sys
import itertools
from markdown_handler import (
    markdown_to_ansi, 
    RED, 
    RESET,
    BOLD, 
    GRAY,
    GREEN,
    YELLOW,
    GREEN_2,
    BLUE
)

def thinking_effect(message="Thinking", stop_event=None):
    """Display a thinking animation in the terminal.
    This function prints a message followed by a series of dots that cycle
    
    Args:
        message (str, optional): The message to display. Defaults to "Thinking".
        stop_event (threading.Event, optional): An event to signal when to stop the animation. Defaults to None.
    If stop_event is provided, the animation will stop when the event is set.
    """
    
    for dot in itertools.cycle([".", "..", "..."]):
        
        if stop_event.is_set():
            break
        
        # Clear the previous line
        sys.stdout.write(f"\r{GRAY}{message}{dot}  {RESET}")
        sys.stdout.flush()
        time.sleep(0.5)
        
    # Clear the line after the animation is done
    sys.stdout.write("\r" + " " * 50 + "\r")
    sys.stdout.flush()

def typewriter(text: str, delay=0.004):
    """
    Print styled ANSI-formatted text character by character.
    """

    styled = markdown_to_ansi(text)

    if not styled.strip():
        return

    i = 0
    while i < len(styled):
        char = styled[i]

        # Print ANSI escape codes instantly (don't delay inside them)
        if char == "\033":
            end = i
            while end < len(styled) and styled[end] != "m":
                end += 1
            end += 1
            sys.stdout.write(styled[i:end])
            sys.stdout.flush()
            i = end
            continue

        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
        i += 1

    print()

def helper() -> str:
    """
    Display a help message with usage instructions.
    
    Returns:
        str: The formatted help message.
    """

    help_message = f"""{BOLD}{GREEN_2}Usage:{RESET} lgpt.py [-h] [--model {{perplexity, gemini, deepseek, llama}}] [-u UPDATE] [-v] [prompt ...]

    {BOLD}{BLUE}Lgpt:{RESET} A command-line utility for managing and interacting with large language models (LLMs) directly from the Linux terminal.

    {BOLD}{YELLOW}Positional arguments:{RESET}
    {GREEN}prompt{RESET}                The prompt to send to the selected model.

    {BOLD}{YELLOW}Optional arguments:{RESET}
    {GREEN}-h{RESET}, {GREEN}--help{RESET}           Show this help message and exit.
    {GREEN}--model{RESET} Model to use {{perplexity, gemini, deepseek, llama}}. Default: {GREEN}deepseek{RESET}.
                            Specify the model to use for query processing.
    {GREEN}-u{RESET} UPDATE, {GREEN}--update{RESET} UPDATE
                            Update Lgpt to the latest version.
    {GREEN}-v{RESET}, {GREEN}--version{RESET}        Display the current version of Lgpt.
    """
    
    return help_message

def error_string_styled(error: str) -> str: return f"{RED}{BOLD}{error}{RESET}"
