import requests
from requests.auth import HTTPBasicAuth


token_url = 'https://api.twitter.com/oauth2/token'
auth = HTTPBasicAuth(
	username='Ttvbd9P66kZ2yiLt2bJrwIDg1', 
	password='gM7WsHxFefkGChj90qldMdTe2XY2pCGkktmf5P7Zim6QeUMQg6'
	)
params = {
	'grant_type': 'client_credentials'
}

def access_token():
	response = requests.post(token_url, data=params, auth=auth)
	if (valid_response := response.json())['token_type'] == 'bearer':
		return valid_response['access_token']
