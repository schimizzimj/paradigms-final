# Marcus Schimizzi

import cherrypy
import re, json
from variables import rdb
from _recipe_database import _recipe_database

class RecommendationsController(object):
	def __init__(self):
		pass

	def DELETE(self):
		rdb.delete_all_ratings() #clear enough
		return json.dumps({'result':'success'})

	def GET_KEY(self, key):
		therecipe = rdb.get_highest_nonrated_recipe(key, rdb.recipes) #this is the recipe id to be recommended
		if therecipe == "-1":#if no such recipe exists, this is a flag
			return json.dumps({'result':'error','message':'no new recipes found'})#error handling
		return json.dumps({'recipe_id': therecipe, 'result':'success'})#return the recipe id

	def PUT_KEY(self, key):
		newrat = json.loads(cherrypy.request.body.read(int(cherrypy.request.headers['Content-Length'])))#get the json from the request
		rdb.set_user_recipe_rating(key, newrat['recipe_id'], newrat['rating'])# get the rating info and add it to the ratings dict
		return json.dumps({'result':'success'})# respond to the request

	def GET_KEY_QUERY(self, key, ingredients):
		ingredient_list = ingredients.split('&')#parse the query string into a list
		refined = rdb.get_recipe_by_ingredient(ingredient_list)# get the recipe dictionary from the ingredient list
		highest = rdb.get_highest_nonrated_recipe(key, refined)#get the best (unrated) of these recipes
		return json.dumps({'recipe_id': highest, 'result': 'success'})#dump out this best recipe
