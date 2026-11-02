"""Model and API configuration, read from the environment."""
import os

from dotenv import dotenv_values


def settings(model_key="LEGO_LLM_MODEL", default_model="gpt-6-astra"):
    """Resolve API settings from the environment, then a local .env."""
    from pathlib import Path

    local = dotenv_values(Path(__file__).resolve().parents[2] / ".env")

    def value(key, default=""):
        return os.environ.get(key) or local.get(key) or default

    base = value("OPENAI_BASE_URL", "https://api.lundong.ai/v1").rstrip("/")
    if not base.endswith("/v1"):
        base += "/v1"
    return dict(
        api_key=value("OPENAI_API_KEY"),
        base_url=base,
        model=value(model_key, value("OPENAI_MODEL", default_model)),
    )
