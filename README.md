# Ollama Python Examples

Small command-line examples that run prompts through a locally hosted Ollama model. The scripts use `llama3.2:latest`.

## Requirements

- Python 3
- [Ollama](https://ollama.com/) installed and running
- The `llama3.2:latest` model downloaded in Ollama
- The Python `ollama` package

## Setup

Pull the model and install the Python package:

```bash
ollama pull llama3.2:latest
python -m pip install ollama
```

Make sure the Ollama service is running before starting a script. If Ollama is not already running as a background service, start it in a separate terminal:

```bash
ollama serve
```

## Run

From this directory, run any example with Python:

```bash
python chatbot.py
```

### Interactive chatbot

`chatbot.py` starts a conversation with a friendly assistant and retains the conversation history for the current run. Enter a message at the `You:` prompt. Type `exit`, `quit`, or `bye` to end the chat.

### Other examples

- `first ai program.py` asks for one prompt and prints a generated response.
- `roles.py` asks for one prompt and sends it to the model with a strict-father system role.

Run the single-prompt examples with quotes around the filename:

```bash
python "first ai program.py"
python roles.py
```

## Project files

| File | Description |
| --- | --- |
| `chatbot.py` | Interactive chat with conversation history |
| `first ai program.py` | Single prompt using Ollama text generation |
| `roles.py` | Single prompt using a system role and chat completion |
