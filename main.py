import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from a .env file if present
load_dotenv()


def get_api_key():
    """Retrieves the API key from environment variables or user input."""
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        print("Error: OPENROUTER_API_KEY not found.")
        print("Please set it in your environment or create a .env file.")
        # For testing purposes only, you could uncomment the line below:
        # api_key = input("Enter your OpenRouter API Key: ").strip()
        sys.exit(1)
    return api_key


def create_client(api_key):
    """Initializes the OpenAI client pointing to OpenRouter."""
    return OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
        # Optional headers required by OpenRouter for rankings/stats
        default_headers={
            "HTTP-Referer": "https://github.com/your-username/my-agent",  # Replace with your site URL
            "X-Title": "My Python Agent",  # Replace with your app name
        }
    )


def main():
    api_key = get_api_key()
    client = create_client(api_key)

    # You can change this to any model on OpenRouter (e.g., "anthropic/claude-3-opus", "google/gemini-2.0-flash-001")
    # "openai/gpt-3.5-turbo" is used here as a reliable default.
    # Check https://openrouter.ai/models for the full list.
    MODEL_NAME = "openai/gpt-3.5-turbo"

    print(f"--- Starting Chat Agent ({MODEL_NAME}) ---")
    print("Type 'quit', 'exit', or 'q' to end the session.\n")

    # Initialize chat history with a system instruction
    conversation_history = [
        {"role": "system", "content": "You are a helpful and concise AI assistant."}
    ]

    while True:
        try:
            user_input = input("You: ").strip()

            if user_input.lower() in ["quit", "exit", "q"]:
                print("Goodbye!")
                break

            if not user_input:
                continue

            # Add user message to history
            conversation_history.append({"role": "user", "content": user_input})

            # Create the completion request
            completion = client.chat.completions.create(
                model=MODEL_NAME,
                messages=conversation_history
            )

            # Extract the response
            bot_response = completion.choices[0].message.content
            print(f"Agent: {bot_response}\n")

            # Add assistant response to history so it remembers the context
            conversation_history.append({"role": "assistant", "content": bot_response})

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            break


if __name__ == "__main__":
    main()