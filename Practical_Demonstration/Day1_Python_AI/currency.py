import requests

BASE = "https://api.frankfurter.app"

from_currency = "USD"
to_currency = "INR"
amount = 1

params = {
    "from": from_currency,
    "to": to_currency,
    "amount": amount
    }

url = f"{BASE}/latest"
#print(url)

try:
    response = requests.get(url, params = params, timeout=10)
    response.raise_for_status()  # raise an exception if the request failed
    data = response.json()
    print(data)
    print(f"{amount} {from_currency} = {data['rates'][to_currency]:.2f} {to_currency}")

except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")









