import requests

from get_bearer_token import access_token


AUTH_HEADER = {'Authorization': f'Bearer {access_token()}'}
BASE_URL = 'https://api.twitter.com/2'


def get_response(verb, url, params=None, data=None, json=None):
	response = requests.request(verb, url, params=params, data=data, json=json, headers=AUTH_HEADER)
	try:
		return response.json()
	except:
		return response.text


def get_tweets():
	all_tweet_objects = []
	search_url = f"{BASE_URL}/tweets/search/recent"
	search_query = {
		'query': 'covid',
		'tweet.fields': 'entities,created_at',
		'user.fields': 'name'
	}
	for _ in range(10):
		response = get_response('get', search_url, params=search_query)
		if isinstance(response, dict):
			next_token = response['meta'].get('next_token')
			if next_token:
				search_query['next_token'] = next_token
			else:
				break
			all_tweet_objects.append(response)

		else:
			print(response)
			break
	return all_tweet_objects


if __name__ == '__main__':
	get_tweets()
