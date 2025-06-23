import time
import sys
import itertools
from markdown_handler import markdown_to_ansi
from markdown_handler import GRAY, RESET

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

def custom_assert(condition: bool, message: str):
    """
    Custom assert function to raise an AssertionError with a message if the condition is False.

    Args:
        condition (bool): The condition to check.
        message (str): The message to display if the assertion fails.
    """
    if not condition:
        typewriter(message)
        sys.exit(1)