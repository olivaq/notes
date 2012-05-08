from django.db import models

# Create your models here.
from datetime import datetime

class Webpage(models.Model):
	url = models.TextField(primary_key=True)

class Note(models.Model):
	note = models.TextField()
	url = models.TextField() #models.ForeignKey('Webpage')
	shared = models.BooleanField(default=False)
	parent = models.ForeignKey('self',blank=True,null=True, related_name='children')
	
	created_date = models.DateTimeField(blank=True,auto_now_add=True)
