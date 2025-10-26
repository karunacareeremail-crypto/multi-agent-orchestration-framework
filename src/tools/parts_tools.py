"""
Parts Lookup Tools

Function tools for handling parts information and compatibility checks.
"""

from typing import Optional, Dict
from agents import function_tool
from ..api.client import api_client


@function_tool
def get_part_details_tool(
    part_number: str, model_number: Optional[str] = None, zip: Optional[str] = None
) -> dict:
    """
    Retrieve part details including compatible models and shipping availability.

    Args:
        part_number (str): Required. The part number to look up.
        model_number (str, optional): If provided, returns compatibility info for only this model.
        zip (str, optional): If provided, includes available shipping methods for the given ZIP code.

    Returns:
        dict: A JSON response with part details, compatible models, and shipping info (if zip provided).
              Example:
              {
                  "statusCode": 200,
                  "body": {
                      "message": {
                          "title": "Pl Spring",
                          "number": "1366",
                          "pricing": {...},
                          "models": {
                              "number": "3352573"
                          },
                          "shipping": [...]
                      }
                  }
              }
    """
    # Build payload dynamically
    payload = {"part_number": part_number}

    if model_number:
        payload["model-number"] = model_number
    if zip:
        payload["zip"] = zip

    try:
        return api_client.post("/parts/lookup", payload)
    except Exception as e:
        return {"statusCode": 500, "error": str(e)}
