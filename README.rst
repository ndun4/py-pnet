=======
py-pnet
=======
A reusable client for the Phish.net API, written in Python3
-----------------------------------------------------------


:Authors:
	Neal Duncan

:Version:
	0.1.0



A Brief Overview
----------------
The reason this library is referred to as a 'client' as opposed to a script or wrapper, is that you import the module, then create a reusable client object. The client object has a few methods for making the actual API calls. This really becomes useful when you need to populate an array with the results from multiple API calls.

Quick-Start
-----------
::

	'''The first thing you must do, as with most Python libraries, is import the required objects. With this library, there's actually only one object (so far), so you'll just import that'''



	from py_pnet import PnetClient



	'''Following the import, the only set-up you need to do before using the client is to create the client object. The constructor for ::class::PnetClient takes your API key as a keyword argument. The default value for ::kwarg::apikey is None. If you leave it as None, the client will still work, but will only be able to get responses from public API methods that phish.net makes available. To gain access to the private API methods, you'll need to supply you API key.'''

	

	pnet = PnetClient(apikey='yourapikey')



	'''From there, you're ready to make the individual API calls. In this example, we're going to make a simple GET request. When calling one of the client's methods, there are 4 arguments the function will take, only one of which is required. The required argument is the ::arg::query_method, which refers to the API methods made available by phish.net. With most of the API methods, there is an available field for a value for the API method being used. There is also a way to filter those results. We'll keep it simple and just fulfill the lone required argument in this example'''



	response = pnet.get(pnet.shows.query)



	'''The new ::variable::response contains the entire response object return by the API call. You may use it however your needs dictate.'''



For a list of all available API methods, please visit api.phish.net.









