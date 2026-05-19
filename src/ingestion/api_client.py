"""ENTSO-E Transparency Platform API client.

Thin wrapper around the REST API with retries, timeouts, and typed
responses. The full client is fleshed out in week 1; this module exists
so the package skeleton is importable from day one.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class EntsoeConfig:
    """Configuration for the ENTSO-E API client.

    Attributes:
        base_url: ENTSO-E Transparency Platform REST endpoint.
        api_token: Personal API token (request one at
            transparency.entsoe.eu → My Account → Web API Security Token).
        timeout_seconds: Per-request timeout.
    """

    base_url: str = "https://web-api.tp.entsoe.eu/api"
    api_token: str = ""
    timeout_seconds: float = 30.0


class EntsoeClient:
    """Client for the ENTSO-E Transparency Platform API.

    Example:
        >>> config = EntsoeConfig(api_token="...")
        >>> client = EntsoeClient(config)
        >>> client.health_check()
        True
    """

    def __init__(self, config: EntsoeConfig) -> None:
        self._config = config

    def health_check(self) -> bool:
        """Lightweight check that the client is wired up correctly.

        Returns True if the API token is set. Real connectivity check
        comes in week 1 once a real endpoint is wired.
        """
        return bool(self._config.api_token)

    # TODO (week 1): implement day-ahead price endpoint
    # def fetch_day_ahead_prices(
    #     self,
    #     bidding_zone: str,
    #     start: datetime,
    #     end: datetime,
    # ) -> list[PriceRecord]:
    #     ...
