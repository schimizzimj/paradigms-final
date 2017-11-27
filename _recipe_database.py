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
			output = self.recipes[rid]
		except KeyError as ex:
			output['result'] = 'error'
			output['message'] = 'key not found'
		return output

	def get_recipe_by_ingredient(self, ingr):
		output = {}
		for arec in self.recipes:
			if ingr.lower() in self.recipes[arec]["ingredients"].lower():
				output[arec] = {}
				output[arec] = self.recipes[arec]
		return output

if __name__ == "__main__":
	rdb = _recipe_database()

	rdb.load_recipes('recipe.txt')
	print(rdb.get_recipe_by_ingredient('seedless'))
