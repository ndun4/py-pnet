import requests

class APIConfig(object):
	"""Defines class to hold static configuration variables"""


	# The only thing you should change in this class is the values in the key dict.
	url = 'https://api.phish.net/'
	endpoint = {'json': 'api.js', 'php': 'api.php'}
	key = {'public': 'pubkey', 'api': 'yourapikey'}
	api_ver = {'2.0': '2.0', '1.0': '1.0'}
	format = {'json': 'json', 'php': 'php'}




class PnetClient(object):
	"""docstring for PnetClient"""

	# Config presets; A sensible default is provided, feel free to change the default config ~OR~
	# modify this library by adding additional presets in dict. format.
	# However, this lib is built on the notion that you'd have a dict of key-value pairs pulling the values
	# in from ::class::APIConfig, so that would be the most straightforward way to change your config presets
	defaults = {'api': APIConfig.api_ver['2.0'], 'format': APIConfig.format['json'], 'apikey': APIConfig.key['api']} 


	# You can replace the value for ::kwarg::endpoint with 'php' for an impromptu request for a php object
	def __init__(self, endpoint='json', config=defaults):
		super(PnetClient, self).__init__()
		
		self.config = config
		self.endpoint = APIConfig.endpoint[endpoint]
		
	# GET method API Call
	def get(self, query_method, query_filter=None, query_filter_value=None, callback=None):

		target = APIConfig.url + self.endpoint
		params = self.config
		params.update({'method': query_method, query_filter: query_filter_value})
		
		r = requests.get(target, params=params)
		return r

	# POST method API Call
	def post(self, query_method, query_filter=None, query_filter_value=None, callback=None):

		target = APIConfig.url + self.endpoint
		params = self.config
		params.update({'method': query_method, query_filter: query_filter_value})
		
		r = requests.post(target, params=params)

		return r








# Making an API call is as simple as:
#pnet = PnetClient()
#print(pnet.get('pnet.shows.setlists.get', query_filter='showdate', query_filter_value='1997-12-31'))
