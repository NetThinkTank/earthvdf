from django.contrib.auth.models import User
from django.contrib.gis.db.models import PointField
from django.db import models


class BaseModel(models.Model):
	class Meta:
		abstract = True

	created = models.DateTimeField(null=False, blank=False, editable=False, auto_now_add=True)

	creator = models.ForeignKey(
		User, related_name='%(app_label)s_%(class)s_creator',
		null=False, blank=False, editable=False
	)

	modified = models.DateTimeField(null=False, blank=False, editable=False, auto_now=True)

	modifier = models.ForeignKey(
		User, related_name='%(app_label)s_%(class)s_modifier',
		null=False, blank=False, editable=False
	)


class Layer(BaseModel):
	name = models.CharField(null=False, blank=False, unique=True, max_length=250)
	slug = models.CharField(null=False, blank=False, unique=True, max_length=50)

	def __unicode__(self):
		return u'%s' % self.name


class Location(BaseModel):
	layer = models.ForeignKey(Layer, related_name='location', null=False, blank=False)

	name = models.CharField(null=False, blank=False, unique=True, max_length=250)
	type = models.CharField(null=False, blank=False, max_length=50)

	point_map = PointField(null=True, blank=True)

	def __unicode__(self):
		return u'%s' % self.name


class Model(BaseModel):
	layer = models.ForeignKey(Layer, related_name='layer', null=False, blank=False)

	name = models.CharField(null=False, blank=False, unique=True, max_length=250)

	dir_url = models.CharField(null=True, blank=True, max_length=250)
	file = models.CharField(null=False, blank=False, max_length=50)

	orientation = models.IntegerField(null=True, blank=True)
	scale = models.IntegerField(null=True, blank=True)

	def __unicode__(self):
		return u'%s' % self.name


class Data(BaseModel):
	class Meta:
		abstract = True
		verbose_name_plural = 'Data'

	key = models.CharField(null=False, blank=False, max_length=50)
	value = models.TextField(null=False, blank=False, max_length=50)

	def __unicode__(self):
		return u'%s: %s' % (self.key, self.value)


class LayerData(Data):
	class Meta:
		verbose_name_plural = 'Layer Data'

	layer = models.ForeignKey(Layer, related_name='layer_data', null=False, blank=False)


class LocationData(Data):
	location = models.ForeignKey(Location, related_name='layer_data', null=False, blank=False)
