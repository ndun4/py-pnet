


import requests


class PnetClient(object):
	"""Defines ::class::PnetClient, which, when instantiated, serves as a reusable client
		for making API calls (i.e. stays running even after an API call is made)"""

	 


	# creates instance of client, supply your API key as a string type for the ::kwarg::apikey
	# although not advisable, you CAN change the values of the other config params
	def __init__(self, apikey=None):
		super(PnetClient, self).__init__()
		self.apikey = apikey
		self.config = {'api': '2.0', 'format': 'json', 'apikey': self.apikey}
		
		
	# GET method API Call, returns a response object akin to what you'd expect from a Requests request
	def get(self, query_method, query_filter=None, query_filter_value=None, callback=None):

		target = 'https://api.phish.net/api.js'
		params = self.config
		params.update({'method': query_method, query_filter: query_filter_value})
		
		r = requests.get(target, params=params)
		return r

	# POST method API Call, like the ::func::get, but for POST
	def post(self, query_method, query_filter=None, query_filter_value=None, callback=None):

		target = 'https://api.phish.net/api.js'
		params = self.config
		params.update({'method': query_method, query_filter: query_filter_value})
		
		r = requests.post(target, params=params)

		return r








