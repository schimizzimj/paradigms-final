# Marcus Schimizzi

import cherrypy
import re, json
from variables import rdb

class RecipesController(object):
	def __init__(self):
		pass

	## General functions
	def GET(self):
		recipes = rdb.get_recipes()
		output = {'result': 'success', 'recipes': recipes}
		return json.dumps(output)

	def POST(self):
		rawData = cherrypy.request.body.read(int(cherrypy.request.headers['Content-Length']))
		data = json.loads(rawData)
		rid = rdb.add_recipe(data)
		output = {'result': 'success', 'id': rid}
		return json.dumps(output)

	def DELETE(self):
		rdb.recipes = {}
		output = {'result': 'success'}
		return json.dumps(output)


	## Key-specific functions
	def GET_KEY(self, key):
		if key in rdb.recipes:
			recipe_output = {}
			recipe_output['result'] = 'success'
			recipe_output['id'] = key
			info = rdb.get_recipe_by_id(key)
			recipe_output['recipe'] = info
		else:
			recipe_output = {'result': 'error', 'message': 'key not found'}
		return json.dumps(recipe_output)

	def PUT(self, key):
		rawData = cherrypy.request.body.read(int(cherrypy.request.headers['Content-Length']))
		data = json.loads(rawData)
		mdb.set_movie(key, data)
		output = {'result': 'success'}
		return json.dumps(output)


	## Ingredient query function
	def GET_QUERY(self, ingredients):
		ingredient_list = ingredients.split('&')
		recipes = rdb.get_recipe_by_ingredient(ingredient_list)
		output = {'result': 'success', 'recipes': recipes}
		return json.dumps(output)
