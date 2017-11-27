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
<<<<<<< HEAD

=======
		
	def load_ratings(self, ratings_file):
		f = open(ratings_file, "r")
		for listing in f:
			listing = listing.strip()
			listing = listing.split("::")
			if int(listing[1]) not in self.ratings:
				self.ratings[int(listing[1])] = {}
			self.ratings[listing[1]][listing[0]] = int(listing[2])	
		f.close()
		
	def get_rating(self, rid):
		counter = 0
		total = 0
		if rid not in self.ratings:
			return {"result":"error", "message":"key not found"}
		thismap = self.ratings[rid]
		for key in thismap:
			total += thismap[key]
			counter += 1
		avgrat=float(total)/float(counter)
		return {"rating":avgrat, "recipe_id":int(rid), "result":"success"}
	def get_highest_rated_recipe(self, user, recipedict):
		current = "0"
		flipped = 1
		for item in recipedict:
			if user in self.ratings[current]:
				current = item
				flipped = 0
			elif self.get_rating(current)['rating'] > self.get_rating(item)['rating']:
				current = item
				flipped = 1
		if flipped == 0:
			return {'result':'error', 'message':'all recipes already rated'}
		else:
			return self.ratings[current]
	
	def set_user_recipe_rating(self, user, rid, rating):
		if rid not in self.ratings:
			self.ratings[rid] = {}
		self.ratings[rid][user] = int(rating)
		
>>>>>>> 0225fce4b521621aab39c18e27ee4eb6f9dcb546
if __name__ == "__main__":
	rdb = _recipe_database()

	rdb.load_recipes('recipe.txt')
	print(rdb.get_recipe_by_ingredient('seedless'))
