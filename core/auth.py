import requests

def login(base_url, username, password):
    print("Logging in with user:", username)

    response = requests.post(
        f"{base_url}/login",
        auth=(username, password)
    )

    if response.status_code != 200:
        raise Exception(
            f"Login failed: {response.status_code} - {response.text}"
        )

    print("Login successful")
    return response.json()["token"]

