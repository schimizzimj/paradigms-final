# Marcus Schimizzi

import cherrypy
import re, json
from variables import rdb

class RecipesController(object):
	def __init__(self):
		pass

	## General functions
	def GET(self):
		recipes = rdb.get_recipes() # get all of the recipes
		output = {'result': 'success', 'recipes': recipes} # put the recipes in a outer json
		return json.dumps(output) # respond to the request

	def POST(self):
		rawData = cherrypy.request.body.read(int(cherrypy.request.headers['Content-Length']))#get the json request data
		data = json.loads(rawData)#make that data a json
		rid = rdb.add_recipe(data)#add the recipe, get the recipe id
		output = {'result': 'success', 'id': rid}#output is status and id of new recipe
		return json.dumps(output)#respond to request

	def DELETE(self):
		rdb.recipes = {}#set the recipe list to empty
		output = {'result': 'success'}#set the response
		return json.dumps(output)#respond to the request


	## Key-specific functions
	def GET_KEY(self, key):#get recipe by id
		if key in rdb.recipes:#check if key exists
			recipe_output = {}#set the output
			recipe_output['result'] = 'success'#set successful result
			recipe_output['id'] = key#set the key
			info = rdb.get_recipe_by_id(key)#get the recipe information
			recipe_output['recipe'] = info#put this recipe information in the output dictionary
		else:
			recipe_output = {'result': 'error', 'message': 'key not found'}#if the key doesn't exits, return that
		return json.dumps(recipe_output)#respond to the request

	def PUT(self, key):
		rawData = cherrypy.request.body.read(int(cherrypy.request.headers['Content-Length']))#get the string from the request
		data = json.loads(rawData)#make the string a json
		rdb.set_recipe(key, data)#use the set recipe to set new information for the recipe
		output = {'result': 'success'}
		return json.dumps(output)#return success message


	## Ingredient query function
	def GET_QUERY(self, ingredients):#this function searches by ingredient
		ingredient_list = ingredients.split('&')#make a list of ingredients from the key
		recipes = rdb.get_recipe_by_ingredient(ingredient_list)#get the list of recipes that have these ingredients
		output = {'result': 'success', 'recipes': recipes}#put them in a dictionary
		return json.dumps(output)#respond to the request
