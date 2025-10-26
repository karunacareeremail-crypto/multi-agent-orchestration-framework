"""
Interactive CLI Demo

An interactive command-line interface for testing the multi-agent orchestration framework.
"""

import asyncio
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file in project root
project_root = Path(__file__).parent.parent
env_path = project_root / ".env"
load_dotenv(dotenv_path=env_path, override=True)

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.agents.orchestrator_agent import create_orchestrator
from agents import Runner


def print_banner():
    """Print welcome banner."""
    print("=" * 70)
    print("🤖 Multi-Agent Orchestration Framework - Interactive Demo")
    print("=" * 70)
    print("\nThis demo showcases an intelligent agent orchestration system that")
    print("routes queries to specialized agents based on intent.")
    print("\nAvailable agents:")
    print("  • Parts Support Agent - Order status, refunds, subscriptions")
    print("  • Parts Sales Agent - Product info, compatibility, shipping")
    print("\nType 'quit' or 'exit' to stop.\n")
    print("=" * 70)


def print_example_queries():
    """Print example queries."""
    print("\n📝 Example Queries You Can Try:")
    print("-" * 70)
    print("Support Queries:")
    print("  • Check order status for order W174191 with zip 20020")
    print("  • Check refund status for order E001861 with ZIP 60179")
    print("  • Get subscription details for membership ID 8282916880")
    print("  • Cancel subscription for membership ID 2237407160")
    print("\nSales Queries:")
    print("  • Need part details for part number 1-17548-006")
    print("  • Details on part 5304495391")
    print("  • Is part 1366 compatible with model 3352573?")
    print("-" * 70)


async def main():
    """Main CLI loop with conversation context."""
    print_banner()
    print_example_queries()

    # Create orchestrator and runner
    orchestrator = create_orchestrator()
    runner = Runner()

    # Initialize conversation context
    conversation_history = []

    print("\n✅ System initialized and ready!")
    print(
        "💡 Conversation context is enabled - the agent will remember previous queries.\n"
    )

    while True:
        try:
            # Get user input
            query = input("🗣️  Your query: ").strip()

            # Check for exit commands
            if query.lower() in {"quit", "exit", "q"}:
                print("\n👋 Goodbye! Thanks for using the demo.")
                break

            # Skip empty queries
            if not query:
                continue

            # Show processing indicator
            print("\n⏳ Processing your query...\n")

            # Build context-aware query
            if conversation_history:
                # Include recent conversation context
                context = "\n\n".join(
                    [
                        f"Previous query: {item['query']}\nPrevious response: {item['response']}"
                        for item in conversation_history[-3:]  # Keep last 3 exchanges
                    ]
                )
                context_aware_query = f"{context}\n\nCurrent query: {query}"
            else:
                context_aware_query = query

            # Run the query through the orchestrator
            result = await runner.run(orchestrator, context_aware_query)

            # Store in conversation history
            conversation_history.append({"query": query, "response": str(result)})

            # Display result
            print("🤖 Response:")
            print("-" * 70)
            print(result)
            print("-" * 70)
            print()

        except KeyboardInterrupt:
            print("\n\n👋 Goodbye! Thanks for using the demo.")
            break
        except Exception as e:
            print(f"\n⚠️  Error occurred: {str(e)}")
            print("Please try again or type 'quit' to exit.\n")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\nExiting...")
