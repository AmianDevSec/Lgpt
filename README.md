<p align="center">
  <img src="lgpt.jpg" alt="Linux GPT Logo" width="100%" height='auto' />
</p>

# Linux GPT (lgpt)

[![GitHub Release](https://img.shields.io/github/v/release/AmianDevSec/Lgpt)](https://github.com/AmianDevSec/Lgpt/releases/latest)

**Lgpt (Linux GPT)** is a lightweight command-line tool that simplifies your Linux terminal experience by integrating powerful large language models (LLMs) — all **without needing API keys**.

<p align="center">
  <img src="https://github.com/user-attachments/assets/fcf764a3-39ba-4ab0-a9c6-3d9a44b22e6b" alt="Linux GPT demo" width="800" height="500" />
</p>

---

## Supported Providers (No API Keys Required)

Lgpt currently supports these providers to process your queries:

* [Deepseek](https://www.deepseek.com/)
* [llama](https://www.ollama.com/)
* [Gemini](https://gemini.google.com)
* [Perplexity](https://www.perplexity.ai)

---

## Usage

Run `lgpt` followed by your query or options:

```bash
Usage: lgpt [-h] [--model {perplexity, gemini, deepseek, llama}] [-u UPDATE] [-v] [prompt ...]

Lgpt — Command-line interface for querying large language models (LLMs) on Linux.

Positional arguments:
  prompt                Your input query or command for the model.

Optional arguments:
  -h, --help            Show this help message and exit.
  --model               Choose model {perplexity, gemini, deepseek, llama}. Default is deepseek.
  -u UPDATE, --update UPDATE
                        Update lgpt to the latest version.
  -v, --version         Show current lgpt version.
````

**Example:**

```bash
lgpt --model gemini "How to update my system packages?"
```

---

## Installation

### GNU/Linux

By default, `lgpt` installs to `/usr/local/bin`. You can change this location as needed but ensure it’s in your system’s `$PATH` for easy use.

Run the following command to install:

```bash
curl -sSL https://raw.githubusercontent.com/AmianDevSec/Lgpt/main/install.sh | bash -s /usr/local/bin
```

After installation, verify by running:

```bash
lgpt --version
```

---

## Uninstallation

If installed via the install script, remove the executable with:

```bash
sudo rm $(which lgpt)
```

---

## Contribution & Support

Feel free to open issues or submit pull requests on the [GitHub repository](https://github.com/AmianDevSec/Lgpt). Contributions and feedback are welcome!

---

## License

This project is licensed under the GPLv3 License. See the [LICENSE](LICENSE) file for details.

---

<p align="center">This project was inspired by <a href="https://github.com/aandrew-me/tgpt" target='_blank' >Terminal GPT(tgpt)</a></p>
```
