"""
Basic Usage Example

Simple example demonstrating how to use the multi-agent orchestration framework.
"""

import asyncio
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.agents.orchestrator_agent import create_orchestrator
from agents import Runner


async def example_order_status_check():
    """Example: Check order status."""
    print("\n" + "=" * 70)
    print("Example 1: Order Status Check")
    print("=" * 70)

    orchestrator = create_orchestrator()
    runner = Runner()

    query = "Check order status for order W174191 with zip 20020"
    print(f"\nQuery: {query}")
    print("\nResponse:")

    result = await runner.run(orchestrator, query)
    print(result)


async def example_refund_check():
    """Example: Check refund status."""
    print("\n" + "=" * 70)
    print("Example 2: Refund Status Check")
    print("=" * 70)

    orchestrator = create_orchestrator()
    runner = Runner()

    query = "Check refund status for order E001861"
    print(f"\nQuery: {query}")
    print("\nResponse:")

    result = await runner.run(orchestrator, query)
    print(result)


async def example_part_lookup():
    """Example: Part details lookup."""
    print("\n" + "=" * 70)
    print("Example 3: Part Details Lookup")
    print("=" * 70)

    orchestrator = create_orchestrator()
    runner = Runner()

    query = "Need part details for part number 1-17548-006"
    print(f"\nQuery: {query}")
    print("\nResponse:")

    result = await runner.run(orchestrator, query)
    print(result)


async def example_subscription_lookup():
    """Example: Subscription lookup."""
    print("\n" + "=" * 70)
    print("Example 4: Subscription Lookup")
    print("=" * 70)

    orchestrator = create_orchestrator()
    runner = Runner()

    query = "Get subscription details for membership ID 8282916880"
    print(f"\nQuery: {query}")
    print("\nResponse:")

    result = await runner.run(orchestrator, query)
    print(result)


async def main():
    """Run all examples."""
    print("\n" + "=" * 70)
    print("🤖 Multi-Agent Orchestration Framework - Basic Usage Examples")
    print("=" * 70)
    print("\nThis script demonstrates basic usage patterns for the framework.")
    print("Each example shows how the orchestrator routes queries to")
    print("specialized agents.\n")

    try:
        # Run examples
        await example_order_status_check()
        await example_refund_check()
        await example_part_lookup()
        await example_subscription_lookup()

        print("\n" + "=" * 70)
        print("✅ All examples completed successfully!")
        print("=" * 70 + "\n")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}\n")


if __name__ == "__main__":
    asyncio.run(main())
