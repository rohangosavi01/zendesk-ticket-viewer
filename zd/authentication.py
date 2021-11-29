import requests

# Importing json File from Zendesk API to read ticket information
url = 'https://zccrgcodingchallenge.zendesk.com/api/v2/tickets.json'
user = 'rohangosavi01@gmail.com' + '/token'
token = 'xk2sED2YCl8hVtRMG37itSVnCBLUNjxljJeBx9i3'

def authenticate_user(url, user, token):

    response = requests.get(url, auth=(user, token))

    if response.status_code != 200:
        return 'error_api_not_available'

    data = response.json()
 
    return data



