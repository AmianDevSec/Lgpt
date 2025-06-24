#!/usr/bin/env bash

## Install script for GNU/Linux
set -e
path=/usr/local/bin

# Check if the system is Linux
if [[ $(uname -s) != "linux" ]]; then
    echo "Unsupported platform $(uname -s)"
    exit 1
fi

# >> Check if curl is installed or nor
if ! command -V curl > /dev/null 2>&1; then
    echo "curl not installed, please install it and try again"
    exit 1
fi

if ! [ -z "$1" ]; then
    path=$1
fi

echo "Download location: $path"

if [ ! -w "$path" ]; then
    SUDO="sudo"
else
    SUDO=""
fi

# Check the system architecture
case $(uname -m) in
    x86_64) ARCH="amd64"   ;;
    arm64 | aarch64) ARCH="arm64"   ;;
    *) echo "Unsupported architecture: $(uname -m)"; exit 1   ;;
esac

[ -e /tmp/lgpt ] && rm /tmp/lgpt

echo -e "Processor Architecture: ${ARCH}\n"

# Set the URL of the executable based on the architecture and OS
URL="https://github.com/AmianDevSec/Lgpt/releases/latest/download/lgpt-${ARCH}"

# Download the executable
echo -e "Downloading...\n"
curl -SL --progress-bar "$URL" -o /tmp/lgpt

# Move the executable to a directory in PATH (e.g. /usr/local/bin/ on Linux, /usr/local/bin/ or /usr/local/opt/ on macOS)
$SUDO mv /tmp/lgpt $path

if [ -d "$path" ]; then
    $SUDO chmod +x $path/lgpt
    elif [ -f "$path" ]; then
    $SUDO chmod +x $path
fi

echo -e "Installed Successfully \n"
echo "Run lgpt -h for help"
