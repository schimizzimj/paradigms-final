# Import needed components
import cherrypy
from _recipe_database import _recipe_database

def start_service():
    d = dict()
    dispatcher = cherrypy.dispatch.RoutesDispatcher()
    resetController = ResetController()
    recipesController = RecipesController()
    recController = RecommendationsController()
    ratingsController = RatingsController()

	### Link up dispatcher to functions
	# Reset Functions
	dispatcher.connect('dict_put', '/reset/',
		controller = resetController, action = 'PUT')

	# Recipe Functions
	dispatcher.connect('recipes_get', '/recipes/',
		controller = recipesController, action = 'GET',
		conditions = dict(method=['GET']))
	dispatcher.connect('recipes_post', '/recipes/',
		controller = recipesController, action = 'POST',
		conditions = dict(method=['POST']))
	dispatcher.connect('recipes_delete', '/recipes/',
		controller = recipesController, action = 'DELETE',
		conditions = dict(method=['DELETE']))
	dispatcher.connect('recipes_get_key', '/recipes/:key',
		controller = recipesController, action = 'GET_KEY',
		conditions = dict(method=['GET']))
	dispatcher.connect('recipes_put', '/recipes/:key',
		controller = recipesController, action = 'PUT',
		conditions = dict(method=['PUT']))
	dispatcher.connect('recipes_get_query', '/recipes/?key=value',
		controller = recipesController, action = 'GET_QUERY',
		conditions = dict(method=['GET']))

	# Recommendation Functions
	dispatcher.connect('rec_delete', '/recommendations/',
		controller = recController, action = 'DELETE',
		conditions = dict(method=['DELETE']))
	dispatcher.connect('rec_get_key', '/recommendations/:key',
		controller = recController, action = 'GET_KEY',
		conditions = dict(method=['GET']))
	dispatcher.connect('rec_put_key', '/recommendations/:key',
		controller = recController, action = 'PUT_KEY',
		conditions = dict(method=['PUT']))

	# Ratings Functions
	dispatcher.connect('ratings_get', '/ratings/:key',
		controller = ratingsController, action = 'GET',
		conditions = dict(method=['GET']))

	# configuration for the server
	conf = {
			'global': {
						'server.socket_host': 'student04.cse.nd.edu',
						'server.socket_port': 51069,
					  },
			'/': {'request.dispatch': dispatcher} }

	# starting the server
	cherrypy.config.update(conf)
	app = cherrypy.tree.mount(None, config=conf)
	cherrypy.quickstart(app)


if __name__ == '__main__':
	start_service()
