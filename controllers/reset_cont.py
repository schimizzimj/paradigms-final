# Marcus Schimizzi

import cherrypy
import re, json
from variables import rdb

class ResetController(object):
	def __init__(self):
		pass

	def PUT(self):
		rdb.init()
