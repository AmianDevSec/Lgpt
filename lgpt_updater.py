import subprocess as sub
from markdown_handler import RED, GREEN, RESET, BOLD
from utils import typewriter, loading_effect, error_string_styled
import threading

# Setup loading animation
stop_event = threading.Event()
loading_thread = threading.Thread(
    target=loading_effect, kwargs={"stop_event": stop_event}
)

def lgpt_updater() -> None:
    output = ""

    try:
        loading_thread.start()
        get_os_arch = sub.run('uname -m', shell=True, capture_output=True, check=True)
        os_arch = get_os_arch.stdout.decode().strip()
        url = f"https://github.com/AmianDevSec/Lgpt/releases/latest/download/lgpt-{os_arch}"

        command = (
            "echo 'Lgpt Updating Started...' && "
            "[ -e /tmp/lgpt ] && rm /tmp/lgpt && "
            f"curl -SL --progress-bar {url} -o /tmp/lgpt && "
            "echo 'Updating Lgpt...' && "
            "sudo mv /tmp/lgpt /usr/local/bin/ && "
            "sudo chmod +x /usr/local/bin/lgpt"
        )

        run_update= sub.run(command, shell=True, capture_output=True, check=True)

        if run_update.stderr :
            output = error_string_styled("Update failed, please try again.")
        else:
            output = f"{GREEN}{BOLD}Update successfully.{RESET}"
            
    except Exception as e :
        output = error_string_styled(f"An error occurred during the update: {e}")
    finally:
        stop_event.set()
        loading_thread.join()

    return typewriter(output)