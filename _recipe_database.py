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

	def load_ratings(self, ratings_file):
		f = open(ratings_file, "r")
		for listing in f:
			listing = listing.strip()
			listing = listing.split("::")
			if listing[0] not in self.ratings:
				self.ratings[listing[0]] = {}
			self.ratings[listing[0]][listing[1]] = int(listing[2])
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

	def get_highest_nonrated_recipe(self, user, recipedict):
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

	def get_highest_rated_recipe(self):
		if self.ratings:
			ratings = {}
			for key in self.ratings:
				ratings[key] = self.get_rating(key)
			max_val = max(ratings.values())
			ratings_max = [key for key in ratings.keys() if ratings[key] == max_val]
			return min(ratings_max)
		else:
			return None

	def set_user_recipe_rating(self, user, rid, rating):
		if rid not in self.ratings:
			self.ratings[rid] = {}
		self.ratings[rid][user] = int(rating)

	def get_user_recipe_rating(self, user, rid):
		if rid not in self.ratings:
			return {'result':'error', 'message':'recipe not found'}
		if user not in self.ratings[rid]:
			return {'result':'error', 'message':'user not found (for this recipe)'}
		else:
			return self.ratings[rid][user]

	def delete_all_all(self):
		self.ratings.clear()
		self.recipes.clear()

	def delete_all_recipes(self):
		self.recipes.clear()

	def delete_all_ratings(self):
		self.ratings.clear()

	def write_recipes(self, filename):
		f = open(filename, "w")
		f.write(json.dumps(self.recipes))
		f.close

	def write_ratings(self, filename):
		f = open(filename, "w")
		for item in self.ratings:
			for uitem in self.ratings[item]:
				thisrating = str(self.ratings[item][uitem])			
				tempstring = item + "::" + uitem + "::" + thisrating + "\n"
				f.write(tempstring)
		f.close()

if __name__ == "__main__":
	rdb = _recipe_database()
	
	rdb.load_ratings('origratings.txt')
	rdb.set_user_recipe_rating('100000', '0', 5)
	rdb.write_ratings('ratings.txt')
