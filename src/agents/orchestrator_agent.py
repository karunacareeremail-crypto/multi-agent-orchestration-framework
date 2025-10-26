"""
Orchestrator Agent

Routes queries to specialized agents based on intent and query type.
"""

from agents import Agent, Runner, function_tool
from .parts_support_agent import create_support_agent
from .parts_sales_agent import create_sales_agent


# Create agent instances
_support_agent = create_support_agent()
_sales_agent = create_sales_agent()
_runner = Runner()


@function_tool
async def parts_support_tool(query: str) -> str:
    """
    Routes queries to the parts support agent for order status, refunds, and subscriptions.

    Use this tool for:
    - Order status inquiries
    - Refund status checks
    - Subscription lookups, updates, or cancellations
    - Customer support related queries

    Args:
        query: The customer's support query

    Returns:
        str: The support agent's response
    """
    result = await _runner.run(_support_agent, query)
    return str(result)


@function_tool
async def parts_sales_tool(query: str) -> str:
    """
    Routes queries to the parts sales agent for product information and compatibility.

    Use this tool for:
    - Part specifications and details
    - Model compatibility checks
    - Shipping availability information
    - Product-related inquiries

    Args:
        query: The customer's sales/product query

    Returns:
        str: The sales agent's response
    """
    result = await _runner.run(_sales_agent, query)
    return str(result)


def create_orchestrator() -> Agent:
    """
    Create and configure the Orchestrator Agent.

    Returns:
        Agent: Configured orchestrator agent that routes to specialized agents
    """
    return Agent(
        name="PartsOrchestratorAgent",
        instructions="""
        You are an intelligent routing agent that directs customer queries to the appropriate specialist.
        You maintain conversation context and understand when customers provide follow-up information.
       
        Your role:
        - Analyze incoming queries AND previous conversation context to understand customer intent
        - Extract information from conversation history when customers provide follow-up details
        - Route to the appropriate specialized agent with ALL relevant information
        - Ensure customers get help from the right expert
       
        Context Handling:
        - When you see "Previous query:" and "Previous response:" in the input, pay attention to the conversation history
        - If the current query is incomplete but provides information related to a previous query, combine them
        - For example:
          * Previous: "Check order W174191" → Current: "60179" → Understand this as "Check order W174191 with zip 60179"
          * Previous: "subscription for water filter" → Current: "512-709-1519" → Understand this as "subscription lookup for phone 512-709-1519"
          * Previous: "looking for subscription" → Current: "8282916880" → Understand this as "subscription lookup for membership ID 8282916880"
        - Extract phone numbers, zip codes, membership IDs, or other details from follow-up messages
       
        Routing guidelines:
       
        Use parts_support_tool for:
        - Order status checks (e.g., "Where is my order?", "Track order W174191")
        - Refund inquiries (e.g., "Refund status for order E001861")
        - Subscription management (e.g., "Cancel my subscription", "Update frequency", "subscription for 512-709-1519")
        - Any customer support related questions
       
        Use parts_sales_tool for:
        - Part information (e.g., "Details for part 5304495391")
        - Compatibility checks (e.g., "Is this part compatible with model X?")
        - Shipping information (e.g., "Shipping options to 90210")
        - Product specifications and availability
       
        Important:
        - Only invoke ONE tool per query
        - Choose the most appropriate tool based on the query intent AND conversation history
        - When you have enough information from context + current query, pass COMPLETE information to the tool
        - If you see a phone number or membership ID in follow-up, treat it as part of a subscription query
        - Let the specialized agent handle the details once you've routed with complete info
        """,
        tools=[parts_support_tool, parts_sales_tool],
    )
