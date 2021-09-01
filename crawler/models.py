from django.db import models

# Create your models here.
class Links(models.Model):
	id = models.IntegerField(primary_key=True)
	link = models.URLField(max_length=200)
	name = models.CharField(max_length=100, default="")

	def __str__(self):
		return self.name

class Comments(models.Model):
	name = models.CharField(max_length=100)
	comment = models.CharField(max_length=10000)
	id = models.AutoField(primary_key=True)

	def __str__(self):
		return (self.name + " - " + str(self.id))
