import requests

# Make a GET request
response = requests.get('https://api.example.com/data')

# Check if request was successful
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")

# POST request example
payload = {'key': 'value'}
response = requests.post('https://api.example.com/submit', json=payload)

# Access response data
print(response.text)  # Raw text
print(response.json())  # Parsed JSON 