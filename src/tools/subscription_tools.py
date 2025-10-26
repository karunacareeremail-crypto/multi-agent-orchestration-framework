"""
Subscription Management Tools

Function tools for handling subscription lookups, updates, and cancellations.
"""

from typing import Dict
from agents import function_tool
from ..api.client import api_client


@function_tool
def parts_subscription_lookup_tool(phone_number: str, membership_id: str) -> dict:
    """
    Fetch the Subscription details for a given membership ID. When membership ID is not provided,
    then retrieves all memberships associated with the phone number passed.

    This function calls the subscription lookup API to retrieve: subscription details such as
    status, creation date, qty, frequency, part details and customer details.

    Args:
        phone_number: Optional. Phone number for which the subscription memberships have to be retrieved
        membership_id: Membership ID the customer would have received when enrolled.
        When both parameters are passed, Membership ID is given priority and the details of the
        subscription associated with that membership ID
        Though both are optional parameters, at least one parameter is expected

    Returns:
        dict: API response structure as follows:
           {
              "statusCode": 200,
              "body": {
                "subscriptionDetails": [
                  {
                    "membershipId": "string",
                    "status": "string",                // e.g., "N" (inactive), "A" (active)
                    "nextFulfillmentDate": "datetime",// ISO 8601 format
                    "quantity": "string",
                    "createdTimestamp": "datetime",
                    "subscriptionId": "string",
                    "renewalPeriodType": "string",    // e.g., "M" for monthly
                    "renewalPeriod": "string",        // e.g., "6" for every 6 months
                    "partsDetail": [...],
                    "customer": {...}
                    }
                  }
                ],
                "message": "string" // e.g., "Orders found for phone number ..."
            }
    """
    payload = {"phoneNumber": phone_number, "membershipId": membership_id}

    try:
        return api_client.post("/subscription/lookup", payload)
    except Exception as e:
        return {"statusCode": 500, "error": str(e)}


@function_tool
def parts_subscription_cancel_tool(membership_id: str) -> dict:
    """
    Cancel a subscription based on the provided membership ID.

    Args:
        membership_id (str): The membership ID of the subscription to be canceled.

    Returns:
        dict: The API response indicating success or failure of the cancellation request.
              Example:
              {
                  "statusCode": 200,
                  "body": {
                      "message": "Subscription canceled successfully."
                  }
              }
    """
    payload = {"membershipId": membership_id}

    try:
        return api_client.post("/subscription/cancel", payload)
    except Exception as e:
        return {"statusCode": 500, "error": str(e)}


@function_tool
def parts_subscription_update_tool(membership_id: str, update: str, value: str) -> dict:
    """
    Update a subscription's frequency or quantity based on the provided membership ID.

    Args:
        membership_id (str): The membership ID of the subscription to update.
        update (str): The type of update to perform. Must be either "frequency" or "quantity".
        value (str): The new value for the selected update type.

    Returns:
        dict: The API response indicating success or failure.
              Example:
              {
                  "statusCode": 200,
                  "body": {
                      "message": "Frequency updated successfully."
                  }
              }
    """
    if update not in ["frequency", "quantity"]:
        return {
            "statusCode": 400,
            "error": "Invalid update type. Must be 'frequency' or 'quantity'.",
        }

    payload = {
        "membershipId": membership_id,
        "update": update,
        update: value,  # Dynamically sets either 'frequency': value or 'quantity': value
    }

    try:
        return api_client.post("/subscription/edit", payload)
    except Exception as e:
        return {"statusCode": 500, "error": str(e)}
