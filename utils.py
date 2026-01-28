import os
import sys
import textwrap
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables once when this module is imported
load_dotenv()

#All the available models for CHXT agent

MODELS = {
    "1": {
        "name": "Google Gemini 2.0 Flash (Free)",
        "id": "google/gemini-2.0-flash-exp:free",
        "desc": "Fast, high context window, great for general tasks."
    },
    "2": {
        "name": "Meta Llama 3.3 70B (Free)",
        "id": "meta-llama/llama-3.3-70b-instruct:free",
        "desc": "Very smart open-source model, GPT-4 class."
    },
    "3": {
        "name": "DeepSeek R1 (Free)",
        "id": "deepseek/deepseek-r1-0528:free",
        "desc": "Excellent at reasoning and coding tasks."
    },
    "4": {
        "name": "Mistral 7B Instruct (Free)",
        "id": "mistralai/mistral-small-3.1-24b-instruct:free",
        "desc": "Reliable, smaller model. Good for quick chats."
    },
    "5": {
        "name": "Nvidia Nemotron3 30B A3B (Free)",
        "id": "nvidia/nemotron-3-nano-30b-a3b:free",
        "desc": "High reasoning capability mixture-of-experts (MOE) model from NVIDIA."
    },
    "6": {
        "name": "OpenAI GPT OSS 120B (Free) - HAS RIGHTS TO PUBLISH CHATS",
        "id": "openai/gpt-oss-120b:free",
        "desc": "OpenAI GPT-OSS model. A Mixture-of-Experts model for reasoning and agentic use cases."
    }
}


def get_api_key():
    """Get API key from environment variables."""
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        print("Error: OPENROUTER_API_KEY not found.")
        print("Please set it in your environment or create a .env file.")
        sys.exit(1)
    return api_key


def create_client(api_key):
    """Create a OpenAI API client to point to OpenRouter"""
    return OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
        default_headers={
            "HTTP-Referer": "https://github.com/your-username/my-agent",
            "X-Title": "Python CLI Agent",
        }
    )


def select_model():
    """Displays a menu and returns the selected model ID."""
    print("\n--- Select an AI Model ---")
    for key, model in MODELS.items():
        print(f"[{key}] {model['name']}")
        print(f"    └─ {model['desc']}")
        print()

    while True:
        choice = input("\nEnter choice (1-5) or 'q' to quit: ").strip()

        # Handle exit commands
        if choice.lower() in ['q', 'quit', 'exit']:
            print("Goodbye!")
            sys.exit(0)

        if choice in MODELS:
            selected = MODELS[choice]
            print(f"\nSelected: {selected['name']}")
            return selected['id']

        print("Invalid choice. Please try again.")


def print_wrapped_response(text, width=100):
    """Prints text wrapped to a specific width while preserving paragraphs."""

    print("\rAgent: \n")

    # Split text by existing newlines to preserve paragraphs/code blocks
    for line in text.splitlines():
        if not line.strip():
            print()
            continue

        # Wrap each line individually
        wrapped_lines = textwrap.wrap(line, width=width)
        for w_line in wrapped_lines:
            print(w_line)

    print()  #Line for spacing