# Import needed components
import cherrypy
from _recipe_database import _recipe_database
from controllers.reset_cont import *
from controllers.recipes_cont import *
from controllers.recommendations_cont import *
from controllers.ratings_cont import *
from controllers.options_cont import *
from controllers.save_cont import *

def CORS():
        cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
        cherrypy.response.headers["Access-Control-Allow-Methods"] = "GET, PUT, POST, DELETE"
        cherrypy.response.headers["Access-Control-Allow-Credentials"] = "*"


def start_service():
    d = dict()
    dispatcher = cherrypy.dispatch.RoutesDispatcher()
    resetController = ResetController()
    recipesController = RecipesController()
    recController = RecommendationsController()
    ratingsController = RatingsController()
    optionsController = OptionsController()
    saveController = SaveController()


	### Link up dispatcher to functions
	# Reset Functions
    dispatcher.connect('dict_put', '/reset/',
        controller = resetController, action = 'PUT')

    # Save Functions
    dispatcher.connect('save_put', '/save/',
        controller = resetController, action = 'PUT')

	# Recipe Functions
    # would have rather used '/recipes/:ingredients', but wouldn't have been
    # differentiated from '/recipes/:key' so this turned out to be a good way to handle it
    # for our usage
    dispatcher.connect('recipes_get_query', '/recipes/query=:ingredients',
        controller = recipesController, action = 'GET_QUERY',
        conditions = dict(method=['GET']))
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
    # Double arguments to be passed to function in this way because it looks better and
    # is a fairly intuitive way to do so
    dispatcher.connect('rec_get_key_query', '/recommendations/:key/:ingredients',
        controller = recController, action = 'GET_KEY_QUERY',
        conditions = dict(method=['GET']))

	# Ratings Functions
    dispatcher.connect('ratings_get', '/ratings/:key',
        controller = ratingsController, action = 'GET',
        conditions = dict(method=['GET']))

    # Connect resources to options controller
    dispatcher.connect(name='reset_connect', route='/reset/',
            controller=optionsController, action='OPTIONS',
            conditions=dict(method=['OPTIONS']))
    dispatcher.connect(name='save_connect', route='/save/',
            controller=optionsController, action='OPTIONS',
            conditions=dict(method=['OPTIONS']))
    dispatcher.connect(name='recipes_connect', route='/recipes/',
            controller=optionsController, action='OPTIONS',
            conditions=dict(method=['OPTIONS']))
    dispatcher.connect(name='recipes_key_connect', route='/recipes/:key',
            controller=optionsController, action='OPTIONS',
            conditions=dict(method=['OPTIONS']))
    dispatcher.connect(name='recipes_query_connect', route='/recipes/query=:ingredients',
            controller=optionsController, action='OPTIONS',
            conditions=dict(method=['OPTIONS']))
    dispatcher.connect(name='recommendations_connect', route='/recommendations/',
            controller=optionsController, action='OPTIONS',
            conditions=dict(method=['OPTIONS']))
    dispatcher.connect(name='recommendations_key_connect', route='/recommendations/:key',
            controller=optionsController, action='OPTIONS',
            conditions=dict(method=['OPTIONS']))
    dispatcher.connect(name='recommendations_key_ingredients_connect', route='/recommendations/:key/:ingredients',
            controller=optionsController, action='OPTIONS',
            conditions=dict(method=['OPTIONS']))
    dispatcher.connect(name='ratings_key_connect', route='/ratings/:key',
            controller=optionsController, action='OPTIONS',
            conditions=dict(method=['OPTIONS']))

	# configuration for the server
    conf = {
            'global': {
                        'server.socket_host': 'student04.cse.nd.edu',
                        'server.socket_port': 51069,
                        },
            '/': {
                'request.dispatch': dispatcher,
                'tools.CORS.on': True
            },
    }

	# starting the server
    cherrypy.config.update(conf)
    app = cherrypy.tree.mount(None, config=conf)
    cherrypy.quickstart(app)


if __name__ == '__main__':
    cherrypy.tools.CORS = cherrypy.Tool('before_finalize', CORS)
    start_service()
