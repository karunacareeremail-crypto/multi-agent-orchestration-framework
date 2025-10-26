"""
Order Management Tools

Function tools for handling order status and refund inquiries.
"""

from typing import Dict
from agents import function_tool
from ..api.client import api_client


@function_tool
def parts_get_order_status_tool(order_no: str, zip: str = "") -> dict:
    """
    Fetch the status of a parts order by order number and optionally a zip code.

    Description:
    This function retrieves the current status and details of a parts order including:
    - Overall order status
    - List of individual parts (with shipping/arrival dates)
    - Customer shipping address

    If multiple orders are found for the given order number, the zip code helps disambiguate.

    Args:
        order_no (str): Required. The order number to look up.
        zip (str, optional): Zip code to validate and filter the order only when multiple orders are found "".

    Returns:
        dict: The API response, which includes:
            {
                "statusCode": int,  # 200 (OK), 201 (Multiple matches), or 404 (Not found)
                "body": {
                    "partOrderDetails": {
                        "orderNumber": str,
                        "status": str,
                        "partsDetail": [...],
                        "customer": {...}
                    },
                    "message": str
                }
            }
    """
    payload = {"orderNo": order_no}
    if zip:
        payload["zip"] = zip

    try:
        return api_client.post("/parts/status", payload)
    except Exception as e:
        return {"error": str(e)}


@function_tool
def parts_get_refund_status_tool(order_no: str, zip: str = "") -> dict:
    """
    Fetch the refund status of a parts order using the order number and optional zip code.

    This function calls the refund status API to retrieve:
    - Refund status of the parts order
    - Associated refund messages or flags

    Args:
        order_no (str): Required. The order number to check refund status for.
        zip (str, optional): Zip code to help disambiguate if multiple orders exist.

    Returns:
        dict: API response structure as follows:
            {
                "statusCode": 200 | 201 | 404,
                "body": {
                    "refundStatus": str,
                    "refundDetails": [
                        {
                            "partNumber": str,
                            "refundAmount": float,
                            "refundStatus": str,
                            "processedDate": str
                        },
                        ...
                    ],
                    "message": str
                }
            }
    """
    payload = {"orderNo": order_no}
    if zip:
        payload["zip"] = zip

    try:
        return api_client.post("/parts/refundstatus", payload)
    except Exception as e:
        return {"error": str(e)}
