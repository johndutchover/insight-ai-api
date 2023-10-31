#!/usr/bin/env python3

import requests
import typer
import logging

app = typer.Typer()

BASE_URL = "https://insight-ai-api.fly.dev/"


def fetch_data(endpoint: str):
    """Fetch data from the API."""
    url = BASE_URL + endpoint
    logging.info(f"{url=}")
    headers = {"Accept": "application/json"}

    response = requests.post(url, headers=headers, timeout=5)

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()


@app.command()
def get_random_fact(n: int):
    """
    Generate a random fact for a given number.
     :param n:
    """
    endpoint = f"facts/fact_for_number?n={n}"
    try:
        data = fetch_data(endpoint)
        typer.echo(data)
    except requests.RequestException as e:
        typer.echo(f"Error fetching data: {e}")


@app.command()
def translate_to_german(word: str):
    """
    Fetch data from the insight-ai-api endpoint.

    Args:
    - endpoint (str): The endpoint to fetch data from. Example: "data/123"
    """

    endpoint = f"translate/translate?text={word}"
    try:
        data = fetch_data(endpoint)
        typer.echo(data)
    except requests.RequestException as e:
        typer.echo(f"Error fetching data: {e}")


if __name__ == "__main__":
    app()
