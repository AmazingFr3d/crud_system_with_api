import requests
import json

BASE = "http://127.0.0.1:5000"
payload = {
    "lead": {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "phone": "123-456-7890"
    },
    "membership": {
        "membership_name": "Gold",
        "level_name": "Premium"
    }
}
headers = {'Content-Type': 'application/json'}  # Specify JSON content type
response = requests.post(f"{BASE}/api/ktr", data=json.dumps(payload), headers=headers)
print(response)