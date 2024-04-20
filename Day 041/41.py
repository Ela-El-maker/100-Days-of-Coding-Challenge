import requests

# Define the base URL of the website
#base_url = 'http://portfolio.felixeladi.co.ke'
base_url = 'www.daystar.ac.ke'

# Define a list of common directory names
directories = ['admin','public', 'backup', 'config', 'includes', 'logs', 'uploads']

# Loop through each directory name
for dir_name in directories:
    # Construct the URL for the directory
    url = f'{base_url}/{dir_name}'

    # Send a GET request to the directory URL
    response = requests.get(url)

    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        print(f'Found directory: {url}')