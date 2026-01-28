from utils import get_api_key, create_client, select_model, print_wrapped_response


def main():
    # Display Startup Banner
    print(r"""
    ###############################################
    ###############################################
    
    $$$$$$\     $$\   $$\   $$\   $$\   $$$$$$$$\ 
    $$  __$$\   $$ |  $$ |  $$ |  $$ |  \__$$  __|
    $$ /  \__|  $$ |  $$ |  \$$\ $$  |     $$ |   
    $$ |        $$$$$$$$ |   \$$$$  /      $$ |   
    $$ |        $$  __$$ |   $$  $$<       $$ |   
    $$ |  $$\   $$ |  $$ |  $$  /\$$\      $$ |   
    \$$$$$$     |$$ |  $$|  $$ /  $$ |     $$ |   
    \______/    \__|  \__|  \__|  \__|     \__|                             
    
    ###############################################
    ###############################################
    """)
    print("   Welcome to CHXT - Your AI Companion")
    print("   " + "-" * 35)

    # 1. Setup Phase
    api_key = get_api_key()

    model_id = select_model()

    client = create_client(api_key)

    # 2. Chat Loop Phase
    print(f"\n--- Starting Chat with {model_id} ---")
    print("Type 'quit', 'exit', or 'q' to end the session.\n")

    conversation_history = [
        {"role": "system", "content": "You are a helpful and concise AI assistant."}
    ]

    while True:
        try:
            user_input = input("You: \n").strip()

            print()

            # Exiting the chat
            if user_input.lower() in ["quit", "exit", "q"]:
                print("Goodbye!")
                break

            if not user_input:
                continue

            conversation_history.append({"role": "user", "content": user_input})

            print("Agent is typing...\n")

            completion = client.chat.completions.create(
                model=model_id,
                messages=conversation_history
            )

            bot_response = completion.choices[0].message.content


            print_wrapped_response(bot_response, width=80)

            conversation_history.append({"role": "assistant", "content": bot_response})

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            break


if __name__ == "__main__":
    main()