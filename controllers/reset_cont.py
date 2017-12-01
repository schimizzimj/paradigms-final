# Marcus Schimizzi
# Luke Napierkowski

import cherrypy
import re, json
from variables import rdb

class ResetController(object):
	def __init__(self):
		pass

	def PUT(self):
		rdb.__init__()
		rdb.load_movies('/data/origrecipe.txt')
		rdb.load_ratings('/data/origratings.txt')
		output = {'result': 'success'}
		return json.dumps(output)
