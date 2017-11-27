import json

class _recipe_database:
	def __init__(self):
		self.recipes = {}
		self.users = {}
		self.ratings = {}
	
	def load_recipes(self, recipe_file):
		self.recipes = json.load(open(recipe_file))
		
	def get_recipe_by_id(self, rid):
		output = {}
		try:
			output = self.recipes[int(rid)]
		except KeyError as ex:
			output['result'] = 'error'
			output['message'] = 'key not found'
		return output
			
	def get_recipe_by_ingredient(self, ingr):
		output = {}
		for arec, arecv in self.recipes:
			if ingr in arec["ingredients"]:
				output[arec] = {}
				output[arec] = arecv
