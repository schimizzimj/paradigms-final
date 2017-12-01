import unittest
import requests
import json

class TestRecipes(unittest.TestCase):

    PORT_NUM = '51069'
    print("Testing Port number: ", PORT_NUM)
    SITE_URL = 'http://student04.cse.nd.edu:' + PORT_NUM
    RECIPES_URL = SITE_URL + '/recipes/'
    RESET_URL = SITE_URL + '/reset/'

    def reset_data(self):
        m = {}
        r = requests.put(self.RESET_URL, data = json.dumps(m))

    def is_json(self, resp):
        try:
            json.loads(resp)
            return True
        except ValueError:
            return False

    def test_recipes_get(self):
        self.reset_data()
        recipe_id = 12
        r = requests.get(self.RECIPES_URL + str(recipe_id))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['name'], 'Yummy Slice-and-Bake Cookies')
        self.assertEqual(resp['datePublished'], '2012-08-15')
        self.assertEqual(resp['url'], 'http://thepioneerwoman.com/cooking/2012/08/yummy-slice-and-bake-cookies/')

    def test_recipes_put(self):
        self.reset_data()
        recipe_id = 105

        r = requests.get(self.RECIPES_URL + str(recipe_id))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['name'], 'Frito Chili Pie')
        self.assertEqual(resp['url'], 'http://thepioneerwoman.com/cooking/2011/09/frito-chili-pie/')

        m = {}
        m['name'] = 'Food'
        m['ingredients'] = 'kiwi, other stuff, a positive attitude'
        r = requests.put(self.RECIPES_URL + str(recipe_id), data = json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')

        r = requests.get(self.MOVIES_URL + str(movie_id))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['name'], m['name'])
        self.assertEqual(resp['ingredients'], m['ingredients'])

    def test_recipes_query(self):
        self.reset_data()

        r = requests.get(self.RECIPES_URL + "query=seedless", data = json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')
        recipe = resp['recipes']['87']
        self.assertEqual(resp['name'], 'Watermelon Granita')

if __name__ == "__main__":
    unittest.main()
