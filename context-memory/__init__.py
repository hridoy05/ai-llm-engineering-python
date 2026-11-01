from .ctx_memory import (
    initialize_client,
    create_initial_messages,
    chat,
    summarize_messages,
    save_conversation,
    load_conversation,
    main as ctx_memory_main,
)

from .no_memory import (
    simple_chat_without_memory,
    main as no_memory_main,
)


def main():
    """Main entry point for the context-memory package.
    
    This function provides a clean interface to access both the context memory
    functionality and the simple memory-less chatbot.
    """
    print("=== Context Memory Package ===")
    print("\nAvailable modes:")
    print("1. Full Context Memory Chat")
    print("2. Simple Chat Without Memory")
    print("\nThe context memory chat maintains conversation history")
    print("and can summarize long conversations to save tokens.")
    print("The simple chat has no memory between messages.")
    
    choice = input("\nSelect a mode (1 or 2): ")
    
    if choice == "1":
        ctx_memory_main()
    elif choice == "2":
        no_memory_main()
    else:
        print("\nInvalid choice. Exiting.")


__all__ = [
    "initialize_client",
    "create_initial_messages", 
    "chat",
    "summarize_messages",
    "save_conversation",
    "load_conversation",
    "simple_chat_without_memory",
    "main",
]
