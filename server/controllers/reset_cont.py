# Marcus Schimizzi
# Luke Napierkowski

import cherrypy
import re, json
from variables import rdb

class ResetController(object):
	def __init__(self):
		pass

	def PUT(self):
		print("resetting")
		rdb.__init__()#set the database to blank
		rdb.load_recipes('data/origrecipe.txt')#load the recipes from original
		rdb.load_ratings('data/origratings.txt')#load the ratings from original
		output = {'result': 'success'}
		return json.dumps(output)#respond to request
