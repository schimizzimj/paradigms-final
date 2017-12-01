# Marcus Schimizzi

import cherrypy
import re, json
from variables import rdb

class RatingsController(object):
	def __init__(self):
		pass

	def GET(self, key):
		return json.dumps({'rating':rdb.get_rating(key), 'recipe_id':key)
