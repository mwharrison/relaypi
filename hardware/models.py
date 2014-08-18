from django.db import models

class Relay(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	name = models.CharField(max_length=200)
	gpio_id = models.PositiveSmallIntegerField()
	
	def __unicode__(self):
		return self.name