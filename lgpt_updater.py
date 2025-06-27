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
        get_os_arch = sub.run('uname -m', shell=True, capture_output=True, check=True)
        os_arch = get_os_arch.stdout.decode().strip()
        arch_name = "amd64" if os_arch == "x86_64" else "arm64"

        url = f"https://github.com/AmianDevSec/Lgpt/releases/latest/download/lgpt-{arch_name}"

        command = (
            f"curl -SL --progress-bar {url} -o /tmp/lgpt && "
            "sudo mv /tmp/lgpt /usr/local/bin/ && "
            "sudo chmod +x /usr/local/bin/lgpt"
        )

        run_update= sub.run(command, shell=True, capture_output=True, check=True)
        output = f"{GREEN}{BOLD}Update successfully.{RESET}" 

    except Exception as e :
        output = error_string_styled(f"An error occurred during the update: {e}")
    except sub.CalledProcessError as e:
        output = error_string_styled(f"Update failed, please try again : {e.stderr.decode()}")
    finally:
        stop_event.set()
        loading_thread.join()

    return typewriter(output)