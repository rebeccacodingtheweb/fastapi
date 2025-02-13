from typing import Optional
import requests

api_key: Optional[str] = None


def get_report(city: str, state: Optional[str], country: str, units: str) -> dict:

    q = f"{city}, {state}, {country}" if state else f"{city}, {country}"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={q}&appid={api_key}&units={units}"

    resp = requests.get(url)
    resp.raise_for_status()

    forecast = resp.json()["main"]
    return forecast
