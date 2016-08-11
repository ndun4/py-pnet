import requests



class PnetClient(object):
	"""docstring for PnetClient"""

	# Config presets; A sensible default is provided, feel free to change the default config ~OR~
	# modify this library by adding additional presets in dict. format.
	# However, this lib is built on the notion that you'd have a dict of key-value pairs pulling the values
	# in from ::class::APIConfig, so that would be the most straightforward way to change your config presets
	 


	# You can replace the value for ::kwarg::endpoint with 'php' for an impromptu request for a php object
	def __init__(self, apikey=None):
		super(PnetClient, self).__init__()
		self.apikey = apikey
		self.config = {'api': '2.0', 'format': 'json', 'apikey': self.apikey}
		
		
	# GET method API Call
	def get(self, query_method, query_filter=None, query_filter_value=None, callback=None):

		target = 'https://api.phish.net/api.js'
		params = self.config
		params.update({'method': query_method, query_filter: query_filter_value})
		
		r = requests.get(target, params=params)
		return r

	# POST method API Call
	def post(self, query_method, query_filter=None, query_filter_value=None, callback=None):

		target = 'https://api.phish.net/api.js'
		params = self.config
		params.update({'method': query_method, query_filter: query_filter_value})
		
		r = requests.post(target, params=params)

		return r








# Making an API call is as simple as:
#pnet = PnetClient()
#print(pnet.get('pnet.shows.setlists.get', query_filter='showdate', query_filter_value='1997-12-31'))
