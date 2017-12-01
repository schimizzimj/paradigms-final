# Marcus Schimizzi

import cherrypy
import re, json
from variables import rdb
from _recipe_database import _recipe_database

class RecommendationsController(object):
	def __init__(self):
		pass

	def DELETE(self):
		rdb.delete_all_ratings()

	def GET_KEY(self, key):
		therecipe = get_highest_nonrated_recipe(key)
		if therecipe == "0":
			return json.dumps({'result':'error','message':'no new recipes found'})
		return json.dumps({'recipe_id': therecipe, 'result':'success'})

	def PUT_KEY(self, key):
		newrat = json.loads(cherrypy.request.body.read(int(cherrypy.request.headers['Content-Length'])))
		rdb.set_user_recipe_rating(key, newrat['recipe_id'], newrat['rating'])
		return json.dumps({'result':'success'})
