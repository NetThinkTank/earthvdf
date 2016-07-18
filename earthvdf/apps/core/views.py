from django.conf import settings
from django.core import serializers
from django.http import HttpResponse

from core.models import Layer, Location, Model, LayerData, LocationData

import json


def ajax_response(text):
	response = HttpResponse(text, content_type='application/json')
	return response


# from http://code.activestate.com/recipes/577346-getattr-with-arbitrary-depth/

def multi_getattr(obj, attr, default = None):
	"""
	Get a named attribute from an object; multi_getattr(x, 'a.b.c.d') is
	equivalent to x.a.b.c.d. When a default argument is given, it is
	returned when any attribute in the chain doesn't exist; without
	it, an exception is raised when a missing attribute is encountered.
	"""

	attributes = attr.split('.')

	for i in attributes:
		try:
			obj = getattr(obj, i)
		except AttributeError:
			if default:
				return default
			else:
				raise

	return obj


def data_dict(data):
	output = {}

	for d in data:
		output[d.key] = d.value

	return output


def data_dict_with_attr(data, attr):
	output = {}

	for d in data:
		index = multi_getattr(d, attr)

		if not index in output:
			output[index] = {}

		output[index][d.key] = d.value

	return output


def index(request):
	return HttpResponse('earthVDF')


def layer(request, slug=''):
	slug = slug.replace('-', '_')

	layers = Layer.objects.filter(slug=slug)

	if len(layers):
		layer = layers[0]
	else:
		return ajax_response('[]')

	layer_data = LayerData.objects.filter(layer=layer)
	layer_data_dict = data_dict(layer_data)

	locations = Location.objects.filter(layer=layer)

	location_data = LocationData.objects.filter(location__in = locations)
	location_data_dict = data_dict_with_attr(location_data, 'location.id')

	models = Model.objects.filter(layer=layer)

	layer_json = serializers.serialize(
		'json',
		[layer],
		# indent=4
	)

	layer_json = layer_json[1:len(layer_json)-1]

	locations_json = serializers.serialize(
		'json',
		locations,
		# indent=4
	)

	models_json = serializers.serialize(
		'json',
		models,
		# indent=4
	)

	layer_data_json = json.dumps(layer_data_dict)
	location_data_json = json.dumps(location_data_dict)

	data_json = '{"layer": %s, "layerData": %s, "locations": %s, "locationData": %s, "models": %s}' % (
		layer_json, layer_data_json, locations_json, location_data_json, models_json
	)

	return ajax_response(data_json)
