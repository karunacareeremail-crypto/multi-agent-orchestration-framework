"""
Parts Support Agent

Handles customer support queries including order status, refunds, and subscription management.
"""

from agents import Agent
from ..tools.order_tools import (
    parts_get_order_status_tool,
    parts_get_refund_status_tool,
)
from ..tools.subscription_tools import (
    parts_subscription_lookup_tool,
    parts_subscription_cancel_tool,
    parts_subscription_update_tool,
)


def create_support_agent() -> Agent:
    """
    Create and configure the Parts Support Agent.

    Returns:
        Agent: Configured support agent with appropriate tools
    """
    return Agent(
        name="PartsSupportAgent",
        instructions="""
        You are a customer support specialist for parts orders and subscriptions.
       
        Your responsibilities:
        - Check order status and provide tracking information
        - Look up refund status and process refund inquiries
        - Manage subscription details (lookup, update, cancel)
        - Provide helpful and accurate information to customers
       
        Important guidelines:
        - Always be polite and professional
        - If you need additional information, ask clarifying questions
        - For order lookups, use the zip code when provided for accuracy
        - Clearly explain the status and next steps to customers
        - Do NOT handle product compatibility or sales-related queries
       
        Use the available tools to gather information and assist customers effectively.
        """,
        tools=[
            parts_get_order_status_tool,
            parts_get_refund_status_tool,
            parts_subscription_lookup_tool,
            parts_subscription_cancel_tool,
            parts_subscription_update_tool,
        ],
    )
