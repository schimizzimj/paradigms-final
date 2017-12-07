# Marcus Schimizzi
# Luke Napierkowski

import cherrypy
import re, json
from variables import rdb

class SaveController(object):
	def PUT(self):
		rdb.write_ratings("data/ratings_new.txt") # save current ratings to file
		output = {'result': 'success'}
		return json.dumps(output)#respond to request
