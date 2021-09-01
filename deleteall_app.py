'''
This module can be run with python3 deleteall_app.py , uncommenting
whichever table you'd like to destroy. 
It was use for testing, experiments etc during the implementation. 
'''

import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "NLP_games.settings")

import django
django.setup()


from crawler.models import Links, Comments
from api.models import Games
# t = Comments.objects.get_or_create()
# Links.objects.all().delete()
# Games.objects.all().delete()

# Comments.objects.all().delete()
