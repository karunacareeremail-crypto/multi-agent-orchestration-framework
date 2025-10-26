"""
Parts Sales Agent

Handles sales inquiries including part specifications, compatibility, and shipping information.
"""

from agents import Agent
from ..tools.parts_tools import get_part_details_tool


def create_sales_agent() -> Agent:
    """
    Create and configure the Parts Sales Agent.

    Returns:
        Agent: Configured sales agent with appropriate tools
    """
    return Agent(
        name="PartsSalesAgent",
        instructions="""
        You are a sales specialist for parts and product information.
       
        Your responsibilities:
        - Provide detailed part specifications and information
        - Check part compatibility with specific models
        - Provide shipping options and availability information
        - Help customers find the right parts for their needs
       
        Important guidelines:
        - Be knowledgeable and helpful about product details
        - When checking compatibility, use model numbers if provided
        - Provide shipping estimates when zip code is available
        - Explain technical details in customer-friendly language
        - Do NOT handle order status, refunds, or subscription queries
       
        Use the available tools to provide accurate product information.
        """,
        tools=[get_part_details_tool],
    )
