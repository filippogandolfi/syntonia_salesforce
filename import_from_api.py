import requests

# Define the API endpoint
url = 'http://example.com/api_endpoint'

# Define the headers for the API request
headers = {
    'Content-Type': 'application/json',
}

# Define the data for the API request
data = {
    'key1': 'value1',
    'key2': 'value2',
}

# Make the POST request
response = requests.post(url, headers=headers, json=data)

# Check if the request was successful
if response.status_code == 200:
    # Write the content of the response to a file
    with open('output.xls', 'wb') as output_file:
        output_file.write(response.content)
else:
    print(f'Request failed with status code {response.status_code}')