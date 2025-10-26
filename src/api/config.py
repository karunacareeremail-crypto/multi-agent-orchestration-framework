"""
API Configuration Module

Manages API endpoints, authentication, and configuration settings.
"""

import os
from typing import Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class APIConfig:
    """Configuration for Parts API."""

    def __init__(self):
        """Initialize API configuration from environment variables."""
        self.base_url = os.getenv(
            "PARTS_API_BASE_URL",
            "https://75krs3hfo2.execute-api.us-east-1.amazonaws.com/dev",
        )
        self.api_key = os.getenv("PARTS_API_KEY", "")
        self.timeout = int(os.getenv("TIMEOUT_SECONDS", "30"))
        self.max_retries = int(os.getenv("MAX_RETRIES", "3"))

    @property
    def headers(self) -> dict:
        """Get default headers for API requests."""
        return {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "x-api-key": self.api_key,
        }

    def get_endpoint(self, path: str) -> str:
        """
        Get full endpoint URL.

        Args:
            path: API endpoint path (e.g., '/parts/status')

        Returns:
            str: Full URL for the endpoint
        """
        return f"{self.base_url}{path}"


class OpenAIConfig:
    """Configuration for OpenAI API."""

    def __init__(self):
        """Initialize OpenAI configuration from environment variables."""
        self.api_key = os.getenv("OPENAI_API_KEY", "")

        # Set the environment variable for OpenAI SDK
        if self.api_key:
            os.environ["OPENAI_API_KEY"] = self.api_key

    @property
    def is_configured(self) -> bool:
        """Check if OpenAI API key is configured."""
        return bool(self.api_key)


# Global configuration instances
api_config = APIConfig()
openai_config = OpenAIConfig()
