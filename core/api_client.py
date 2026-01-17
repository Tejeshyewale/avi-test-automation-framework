import requests

class APIClient:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {token}"
        }

    def get(self, endpoint):
        response = requests.get(
            f"{self.base_url}{endpoint}",
            headers=self.headers
        )
        response.raise_for_status()
        data = response.json()

        # 🔑 FIX: always return list if results exist
        return data.get("results", data)

    def put(self, endpoint, payload):
        response = requests.put(
            f"{self.base_url}{endpoint}",
            json=payload,
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()
