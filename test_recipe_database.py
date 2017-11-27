from _recipe_database import _recipe_database
import unittest

class TestRecipeDatabase(unittest.TestCase):
    '''Unit tests for our final API'''

    rdb = _recipe_database()

    def reset_data(self):
        # self.rdb.delete_ratings()
        self.rdb.load_recipes('recipe.txt')
        # self.rdb.load_ratings('ratings.txt')

    def test_get_recipe_by_id(self):
        self.reset_data()
        recipe = self.rdb.get_recipe_by_id('2')
        self.assertEquals(recipe['name'], 'Herb Roasted Pork Tenderloin with Preserves')
        self.assertEquals(recipe['datePublished'], '2011-09-15')

    def test_get_recipe_by_ingredient(self):
        self.reset_data()
        recipes = self.rdb.get_recipe_by_ingredient('green hot chilies')
        self.assertEquals(recipes['559']['name'], 'Green Curry with Tofu')
        self.assertEquals(recipes['740']['recipeYield'], 'Serves 4.')

    def test_get_recipe_null(self):
        self.reset_data()
        recipe = self.rdb.get_recipe_by_id('3000')
        self.assertEquals(recipe['result'], 'error')

    def test_get_highest_rated_recipe(self):
        self.reset_data()
        rid = self.rdb.get_highest_rated_recipe()

if __name__ == "__main__":
    unittest.main()
