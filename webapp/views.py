from django.shortcuts import render
from functools import partial
import json
from os.path import *
import urllib.request

with urllib.request.urlopen("http://api.ipstack.com/128.210.106.81?access_key=b82a160e56c63c1ca80100eee67690fa&format=1") as url:
	data = json.loads(url.read().decode())
	data["capital"] = data["location"]["capital"]
	data["language"] = data["location"]["languages"][0]["native"]
index = partial(render, template_name="webapp/home.html", context=data)
index.__doc__ = 'Opens the main page of the webapp.'

with open(join(dirname(realpath(__file__)), "team.json"), 'r') as team:
	team = partial(render, template_name="webapp/team.html", context=json.load(team))
	team.__doc__ = 'Opens the team page of the webapp.'
