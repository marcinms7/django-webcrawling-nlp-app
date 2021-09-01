from django.db import models

# Create your models here.
class Games(models.Model):
	name = models.CharField(max_length=100)
	id = models.IntegerField(primary_key=True)
	rating = models.CharField(max_length=100)
	# img = models.URLField(max_length=100)
	imgback = models.URLField(max_length=100)
	metacritic = models.FloatField()
	# subreddit = models.CharField(max_length=100)
	def __str__(self):
		return self.name
