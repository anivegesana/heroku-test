from django.shortcuts import render
from functools import partial

index = partial(render, template_name="webapp/home.html")
index.__doc__ = 'Opens the main page of the webapp.'
