import json

class _recipe_database:
	def __init__(self):#initializes data dictionaries
		self.recipes = {}
		self.ratings = {}

	def get_recipes(self):
		return self.recipes

	def load_recipes(self, recipe_file):#loads in all recipe data from file using json library
		f = open(recipe_file, "r")
		self.recipes = json.load(f)
		f.close()

	def get_recipe_by_id(self, rid):# access a recipe by its id, as in movie database
		output = {}
		try:
			output = self.recipes[rid]#see if id exists
		except KeyError as ex:#if not show error
			output['result'] = 'error'
			output['message'] = 'key not found'
		return output#return dictionary if it exists

	def get_recipe_by_ingredient(self, listOIngredients):#searches for all recipes that use a certain ingredient
		output = {}
		found = 0
		for arec in self.recipes:#loop through all recipes
			found = 1
			for food in listOIngredients:
				if food.lower() not in self.recipes[arec]["ingredients"].lower():#check if ingredient string is in ingredients (using all lower case)
					found = 0
			if found == 1:
				output[arec] = {}#add any results to output dictionary
				output[arec] = self.recipes[arec]
		return output

	def set_recipe(self, rid, info):
		self.recipes[rid] = info

	def add_recipe(self, datadict):
		current = 0
		for keys in self.recipes:#find highest recipe id
			if int(keys) > current:
				current = int(keys)
		self.recipes[str(current+1)] = datadict#make the data dictionary the value of a key that is the new greatest recipe id
		return str(current+1)

	def load_ratings(self, ratings_file):# load all ratings from file
		f = open(ratings_file, "r")#open file
		for listing in f:#go though each line
			listing = listing.strip()
			listing = listing.split("::")#separate parts into a list
			if listing[0] not in self.ratings:#create dictionary if need be
				self.ratings[listing[0]] = {}
			self.ratings[listing[0]][listing[1]] = int(listing[2])#save user-score pair in dictionary corresponding to recipe id
		f.close()

	def get_rating(self, rid):
		counter = 0
		total = 0
		if rid not in self.ratings:#if the recipe doesn't exist, return an error
			return {"result":"error", "message":"key not found"}
		thismap = self.ratings[rid]
		for key in thismap:#go through all users in recipe dictionary
			total += thismap[key]#add the rating to the total
			counter += 1#increment the counter
		avgrat=float(total)/float(counter)#divide total by counter to find average rating
		return avgrat

	def get_highest_nonrated_recipe(self, user, recipedict):
		current = "0"#set an initial recipe
		flipped = 1#flag variable to check if all recipes have been rated
		for item in recipedict:#for all recipes in the given dictionary (this allows for ingredient search)
			if user in self.ratings[current]:#if the user has rated it already
				current = item#move on to the next recipe
				flipped = 0#set the flag to represent that the most recent recipe was already rated
			elif self.get_rating(current) > self.get_rating(item):# if the recipe is unrated by the user and the best checked yet
				current = item#set it as the current best
				flipped = 1#set the flag to indicate it has not been rated
			print("{} > {}".format(self.get_rating(current), self.get_rating(item)))
		if flipped == 1:
			return current
		else:
			return '-1'

	def get_highest_rated_recipe(self):
		# used to get the highest rated recipe overall
		if self.ratings: # check to make sure ratings exists
			ratings = {}
			for key in self.ratings: # get the average rating for each rated recipe
				ratings[key] = self.get_rating(key)
			max_val = max(ratings.values()) # find maximum average rating
			ratings_max = [key for key in ratings.keys() if ratings[key] == max_val]
			# in the case of a tie, only return recipe with lowest idea
			return min(ratings_max)
		else:
			return None

	def set_user_recipe_rating(self, user, rid, rating):
		if rid not in self.ratings:#add the recipe if it doesn't exist
			self.ratings[rid] = {}
		self.ratings[rid][user] = int(rating)#set the rating for the user

	def get_user_recipe_rating(self, user, rid):
		if rid not in self.ratings:# if the recipe doesn't exits, return an error
			return {'result':'error', 'message':'recipe not found'}
		if user not in self.ratings[rid]:# if the user hasn't rated it, return an error
			return {'result':'error', 'message':'user not found (for this recipe)'}
		else:#otherwise return the rating
			return self.ratings[rid][user]

	def delete_all_all(self):#clear all data (for reset, probably)
		self.ratings.clear()
		self.recipes.clear()

	def delete_all_recipes(self):#clear only recipe data
		self.recipes.clear()

	def delete_all_ratings(self):#clear only rating data
		self.ratings.clear()

	def write_recipes(self, filename):#write the current recipe data to the file to save it
		f = open(filename, "w")
		f.write(json.dumps(self.recipes))
		f.close

	def write_ratings(self, filename):#save the current rating data
		f = open(filename, "w")#open file
		for item in self.ratings:#loop through all recipes
			for uitem in self.ratings[item]:#loop through all of the ratings for this recipe
				thisrating = str(self.ratings[item][uitem])#get the rating value as a string
				tempstring = item + "::" + uitem + "::" + thisrating + "\n" #combine strings formatted for the file in rid::uid::rating form
				f.write(tempstring)#write this to the file
		f.close()

if __name__ == "__main__":#test stuff
	rdb = _recipe_database()

	rdb.load_ratings('origratings.txt')
	rdb.set_user_recipe_rating('100000', '0', 5)
	rdb.write_ratings('ratings.txt')
