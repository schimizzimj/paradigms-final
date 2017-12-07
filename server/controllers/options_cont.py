# Marcus Schimizzi
# Luke Napierkowski

import cherrypy
import re, json
from variables import rdb

class OptionsController(object):
	def OPTIONS(self, *args, **kargs):
		return ""
