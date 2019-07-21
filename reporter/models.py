from __future__ import unicode_literals
from django.db import models


class Incidences(models.Model):
	name = models.CharField(max_length=100)
	location = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Incidences'