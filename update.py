import subprocess as sub
def update() -> None:
    try:
        get_os_arch = sub.run('uname -m', shell=True, capture_output=True, check=True)
        os_arch = get_os_arch.stdout.decode().strip()
        url = f"https://github.com/AmianDevSec/Lgpt/releases/latest/download/lgpt-{os_arch}"

        command = (
            "echo 'Lgpt Updating Started...' &&"
            f"curl -SL --progress-bar {url} -o /tmp/lgpt && "
            "echo 'Updating Lgpt...' && "
            "sudo mv /tmp/lgpt /usr/local/bin/lgpt && "
            "sudo chmod +x /usr/local/bin/lgpt"
        )
        
        sub.run(command, shell=True, check=True)

    except Exception as e :
        print(f'An error occured : {e}')