# frontend/src/service/api.py
import httpx
import traceback
from service.auth_context import auth_context

BASE_URL = "http://127.0.0.1:8000"

async def api_request(endpoint, method="GET", json=None, token=None):
    headers = {"Content-Type": "application/json"}
    token = token or auth_context.token
    if token:
        headers["Authorization"] = f"Bearer {token}"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.request(
                method=method,
                url=f"{BASE_URL}{endpoint}",
                json=json,
                headers=headers,
                timeout=10
            )

            # ✅ Verifica si el status code es exitoso
            if response.status_code >= 200 and response.status_code < 300:
                return response.json()
            else:
                try:
                    error_data = response.json()
                    error_detail = error_data.get("detail", f"HTTP {response.status_code}")
                except Exception:
                    error_detail = response.text or f"HTTP {response.status_code}"

                print(f"API responded with status {response.status_code}")
                print("Error detail:", error_detail)

                return {
                    "success": False,
                    "error": error_detail
                }


        except httpx.RequestError as e:
            print("API request error:", type(e).__name__)
            traceback.print_exc()
            return {"success": False, "error": str(e)}