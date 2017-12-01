import unittest
import requests
import json

class TestRatings(unittest.TestCase):

    PORT_NUM = '51069'
    print("Testing Port number: ", PORT_NUM)
    SITE_URL = 'http://student04.cse.nd.edu:' + PORT_NUM
    RATINGS_URL = SITE_URL + '/ratings/'
    RESET_URL = SITE_URL + '/reset/'

    def reset_data(self):
        m = {}
        r = requests.put(self.RESET_URL)

    def is_json(self, resp):
        try:
            json.loads(resp)
            return True
        except ValueError:
            return False

    def test_ratings_get(self):
        self.reset_data()
        recipe_id = '420'

        r = requests.get(self.RATINGS_URL + recipe_id)
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['rating'], 2.875)
        self.assertEqual(resp['recipe_id'], recipe_id)

if __name__ == "__main__":
    unittest.main()
