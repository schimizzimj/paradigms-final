# Used so that every controller may access the same instance of the database

from _recipe_database import _recipe_database

rdb = _recipe_database()
rdb.load_recipes('data/origrecipe.txt')
rdb.load_ratings('data/origratings.txt')
