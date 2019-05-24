from django.db import models

# Create your models here.
class player(models.Model):
	name = models.CharField(max_length=50)
	age = models.IntegerField()
	school_year = models.IntegerField()
	position = models.CharField(max_length=50)
	height = models.IntegerField()
	weight = models.IntegerField()

	




