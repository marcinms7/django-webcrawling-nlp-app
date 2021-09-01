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
