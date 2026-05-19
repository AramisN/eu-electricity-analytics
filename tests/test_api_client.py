"""Tests for the ENTSO-E API client skeleton.

These tests prove the package skeleton is wired correctly. Real endpoint
tests get added in week 1 alongside the actual implementation.
"""

from __future__ import annotations

import pytest

from ingestion.api_client import EntsoeClient, EntsoeConfig


def test_config_defaults_to_official_base_url() -> None:
    config = EntsoeConfig()
    assert config.base_url == "https://web-api.tp.entsoe.eu/api"
    assert config.timeout_seconds == 30.0


def test_health_check_fails_without_token() -> None:
    client = EntsoeClient(EntsoeConfig(api_token=""))
    assert client.health_check() is False


def test_health_check_passes_with_token() -> None:
    client = EntsoeClient(EntsoeConfig(api_token="fake-token-for-test"))
    assert client.health_check() is True


@pytest.mark.parametrize(
    "token, expected",
    [
        ("", False),
        ("real-looking-token-12345", True),
        ("   ", True),  # any non-empty string counts; tighten later if needed
    ],
)
def test_health_check_parametrized(token: str, expected: bool) -> None:
    client = EntsoeClient(EntsoeConfig(api_token=token))
    assert client.health_check() is expected
