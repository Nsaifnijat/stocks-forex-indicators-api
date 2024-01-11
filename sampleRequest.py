import requests

# Set the URL of the Flask server
url = 'http://127.0.0.1:5001/bollinger'

# Define query parameters
params = {
    'symbol': 'AAPL',
    'start_date': '2023-01-01',
    'end_date': '2023-12-31',
    'length': 20
}

# Send GET request to the Flask server
response = requests.get(url, params=params)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Access the parsed data
    datetime_index = data['datetime_index']
    bollinger_bands = data['bollinger_bands']
    # Parse the bollinger_bands data
    bbm = bollinger_bands['BBM_20_2.0']
    bbu = bollinger_bands['BBU_20_2.0']
    bbl = bollinger_bands['BBL_20_2.0']

    # Print or further process the parsed data
    print("Datetime Index:", datetime_index)
    print("BBM:", bbm)
    print("BBU:", bbu)
    print("BBL:", bbl)

else:
    print(f"Error: {response.status_code}\n{response.text}")
