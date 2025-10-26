"""
API Client Module

Handles HTTP requests to the Parts API with error handling and retry logic.
"""

import requests
from typing import Dict, Any, Optional
from .config import api_config


class APIClient:
    """HTTP client for Parts API interactions."""

    def __init__(self, config=None):
        """
        Initialize the API client.

        Args:
            config: Optional APIConfig instance. Uses global config if not provided.
        """
        self.config = config or api_config

    def post(self, endpoint: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Make a POST request to the API.

        Args:
            endpoint: API endpoint path (e.g., '/parts/status')
            payload: Request payload dictionary

        Returns:
            dict: API response as dictionary

        Raises:
            APIError: If the request fails
        """
        url = self.config.get_endpoint(endpoint)

        try:
            response = requests.post(
                url,
                json=payload,
                headers=self.config.headers,
                timeout=self.config.timeout,
            )

            # Handle successful responses
            if response.status_code in [200, 201, 404]:
                return response.json()

            # Handle unexpected status codes
            return {
                "error": f"Unexpected status code: {response.status_code}",
                "details": response.text,
            }

        except requests.exceptions.Timeout:
            return {"error": "Request timeout", "details": "The API request timed out"}

        except requests.exceptions.ConnectionError:
            return {
                "error": "Connection error",
                "details": "Failed to connect to the API",
            }

        except requests.exceptions.RequestException as e:
            return {"error": "Request failed", "details": str(e)}

        except Exception as e:
            return {"error": "Unexpected error", "details": str(e)}


# Global client instance
api_client = APIClient()
