from _recipe_database import _recipe_database
import unittest

class TestRecipeDatabase(unittest.TestCase):
    '''Unit tests for our final API'''

    rdb = _recipe_database()

    def reset_data(self):
        ''' reset the data for ratings to make sure tests work as expected '''
        self.rdb.delete_all_ratings()
        self.rdb.load_recipes('recipe.txt')
        self.rdb.load_ratings('ratings.txt')

    def test_get_recipe_by_id(self):
        ''' test that you can successfully get a recipe by id '''
        self.reset_data()
        recipe = self.rdb.get_recipe_by_id('2')
        self.assertEquals(recipe['name'], 'Herb Roasted Pork Tenderloin with Preserves')
        self.assertEquals(recipe['datePublished'], '2011-09-15')

    def test_get_recipe_by_ingredient(self):
        ''' make sure api correctly performs search based on ingredient '''
        self.reset_data()
        recipes = self.rdb.get_recipe_by_ingredient('green hot chilies')
        self.assertEquals(recipes['559']['name'], 'Green Curry with Tofu')
        self.assertEquals(recipes['740']['recipeYield'], 'Serves 4.')

    def test_get_recipe_null(self):
        '''
            check to see if api correctly handles an attempt to get recipe by
            id that does not exist
        '''
        self.reset_data()
        recipe = self.rdb.get_recipe_by_id('3000')
        self.assertEquals(recipe['result'], 'error')

    def test_get_highest_nonrated_recipe(self):
        ''' test that you can successfully get the highest unrated recipe '''
        self.reset_data()
        rid = self.rdb.get_highest_nonrated_recipe('6', self.rdb.recipes)
        rating = self.rdb.get_rating(rid)
        recipe = self.rdb.get_recipe_by_id(rid)
        self.assertEquals(recipe['name'], 'Almond Soba Noodles Recipe')
        self.assertEquals(rating, 1.4)

    def test_get_highest_rated_recipe(self):
        ''' test to find highest rated recipe overall '''
        self.reset_data()
        rid = self.rdb.get_highest_rated_recipe()
        self.assertEquals(rid, '206')

    def test_set_user_recipe_rating(self):
        ''' test that setting a rating for a user works properly '''
        self.reset_data()
        self.rdb.set_user_recipe_rating('6', '206', 2)
        rating = self.rdb.get_rating('206')
        self.assertEquals(rating, 4.3333333333333333)

if __name__ == "__main__":
    unittest.main()
