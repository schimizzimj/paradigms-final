import unittest
import requests
import json
import sys

class TestMoviesIndex(unittest.TestCase):

    PORT_NUM = '51069'
    print("Testing port number: ",PORT_NUM)
    SITE_URL = 'http://student04.cse.nd.edu:' + PORT_NUM
    RECIPES_URL = SITE_URL + '/recipes/'
    RESET_URL = SITE_URL + '/reset/'

    def reset_data(self):
        m = {}
        r = requests.put(self.RESET_URL, json.dumps(m))

    def is_json(self, resp):
        try:
            json.loads(resp)
            return True
        except ValueError:
            return False

    def test_recipes_index_get(self):
        self.reset_data()
        r = requests.get(self.RECIPES_URL)
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())

        recipes = resp['recipes']
        for recipe in recipes:
            if recipe['id'] == '32':
                testrecipe = recipe

        self.assertEqual(testrecipe['name'], 'Chicken with Mustard Cream Sauce')
        self.assertEqual(testrecipe['prepTime'], 'PT5M')

    def test_movies_index_post(self):
        self.reset_data()

        m = {}
        m['name'] = 'Pizza'
        m['ingredients'] = 'dough, pepperoni, cheese'
        r = requests.post(self.RECIPES_URL, data = json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(resp['id'], '1042')

        r = requests.get(self.RECIPES_URL + resp['id'])
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['name'], m['name'])
        self.assertEqual(resp['ingredients'], m['ingredients'])

    def test_movies_index_delete(self):
        self.reset_data()

        m = {}
        r = requests.delete(self.RECIPES_URL, data = json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')

        r = requests.get(self.RECIPES_URL)
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        movies = resp['recipes']
        self.assertFalse(movies)

if __name__ == "__main__":
    unittest.main()
