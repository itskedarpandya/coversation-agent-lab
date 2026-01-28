# CHXT - Python CLI AI Agent

A lightweight, terminal-based conversational agent built in Python. This project connects to [OpenRouter.ai](https://openrouter.ai) to access a variety of powerful Large Language Models (LLMs) including free options from Google, Meta, and Mistral.

## 🚀 Features

* **Multi-Model Support:** Instantly switch between models like Gemini 2.0 Flash, Llama 3, Mistral, NVIDIA Nemotron 3 and OpenAI GPT via a simple selection menu.
* **Cost-Efficient:** Configured by default to prioritize free-tier models to keep running costs at zero.
* **Terminal UI:** Includes ASCII art branding ("CHXT") and neat text wrapping for readability in the command line.
* **Modular Design:** Clean separation between business logic (`main.py`) and configuration (`utils.py`).
* **Secure:** Uses environment variables to protect API keys.

## 🛠️ Prerequisites

* **Python 3.8+** installed on your system.
* An **OpenRouter API Key** (Get one [here](https://openrouter.ai/keys)).

## 📥 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/itskedarpandya/coversation-agent-lab.git
   cd conversation-agent-lab
   ```

2. **Create a virtual environment (Recommended):**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Mac/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Configuration

1. Refer to the `.env.example` file in the root directory to see the required format.
2. Create a file named `.env` in the root directory (or copy `.env.example` to `.env`):
   ```bash
   cp .env.example .env
   ```
3. Open the `.env` file and replace the placeholder with your actual OpenRouter API key:
   ```env
   OPENROUTER_API_KEY=sk-or-v1-your-actual-key-here
   ```
   *(Note: The `.env` file is hidden by default and ignored by Git for security.)*

## 🖥️ Usage

Run the main script to start the agent:

```bash
python main.py
```

1. Select a model from the numbered menu (1-5).
2. Type your message to chat.
3. Type `q`, `quit`, or `exit` to close the program.

## 📂 Project Structure

* `main.py`: The entry point. Handles the chat loop and user input.
* `utils.py`: Contains configuration, model definitions, API client setup, and helper functions.
* `requirements.txt`: List of Python dependencies.
* `.env`: (Not committed) Stores your private API key.