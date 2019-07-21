from __future__ import unicode_literals
from django.db.models import Manager as GeoManager
from django.contrib.gis.db import models


class Incidences(models.Model):
	name = models.CharField(max_length=100)
	location = models.PointField(srid=3000)
	objects = GeoManager()

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Incidences'