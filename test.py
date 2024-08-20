import requests

headers = {
    'Authorization': 'ExponentPushToken[5eRsJOLWTZs-qjJmGT90wb]',  # Replace with your actual Expo token
    'ClientId': 'f359bd32-97d9-431a-a693-a8c3d032008d',            # Replace with your actual client ID
}

# Assuming you are making a GET request to check access
url = 'https://platform.sparelabs.com/checkAccess'
response = requests.get(url, headers=headers)

if response.status_code == 200:
    try:
        json_data = response.json()
        print(json_data)
    except requests.exceptions.JSONDecodeError:
        print(f"Response is not valid JSON. Raw content:\n{response.text}")
else:
    print(f"Request failed with status code {response.status_code}. Raw content:\n{response.text}")
