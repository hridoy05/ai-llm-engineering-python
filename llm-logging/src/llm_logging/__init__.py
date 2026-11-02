from .chatbot_logging import main

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nChat session ended by user. Goodbye! 👋")
