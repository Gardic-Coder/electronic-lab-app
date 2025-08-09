import requests
import flet as ft

BASE_URL = "http://localhost:8000"

def api_request(endpoint, method="GET", json=None, token=None):
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    
    try:
        response = requests.request(
            method,
            f"{BASE_URL}{endpoint}",
            json=json,
            headers=headers,
            timeout=10
        )
        return response
    except requests.exceptions.RequestException as e:
        print(f"API request error: {e}")
        return None