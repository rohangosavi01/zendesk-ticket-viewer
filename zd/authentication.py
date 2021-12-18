import requests

# Importing json File from Zendesk API to read ticket information
url = ''
user = '' + '/token'
token = '' 

def authenticate_user(url, user, token):

    response = requests.get(url, auth=(user, token))

    if response.status_code != 200:
        return 'error_api_not_available'

    data = response.json()
 
    return data



