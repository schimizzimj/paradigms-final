import unittest
import requests
import json

class TestRecommendations(unittest.TestCase):

    PORT_NUM = '51069'
    print("Testing Port number: ", PORT_NUM)
    SITE_URL = 'http://student04.cse.nd.edu:' + PORT_NUM
    RECOMMENDATIONS_URL = SITE_URL + '/recommendations/'
    RATINGS_URL = SITE_URL + '/ratings/'
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

    def test_recommendations_get(self):
        self.reset_data()
        user_id = 300
        r = requests.get(self.RECOMMENDATIONS_URL + str(user_id))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['recipe_id'], 684)

    def test_recommendations_put(self):
        self.reset_data()
        user_id = 300
        recipe_id = 17
        rating = 5

        m = {}
        m['recipe_id'] = recipe_id
        m['rating'] = rating
        r = requests.put(self.RECOMMENDATIONS_URL + user_id, data = json.dumps(m))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')

        r = requests.get(self.RATINGS_URL + recipe_id)
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['rating'], 3.5714285714285716) 

if __name__ == "__main__":
    unittest.main()
