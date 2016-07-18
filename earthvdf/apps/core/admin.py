from django.conf import settings

from django.contrib import admin
from django.contrib.gis.geos import Point
from django.contrib.gis.admin.options import OSMGeoAdmin

from core.models import \
	Layer, Location, Model, \
	LayerData, LocationData


class BaseAdmin(admin.ModelAdmin):
	def save_model(self, request, obj, form, change):
		if not change:
			obj.creator = request.user

		obj.modifier = request.user
		obj.save()


class LocationAdmin(OSMGeoAdmin):
	default_zoom = 13

	lon = settings.DEFAULT_LON
	lat = settings.DEFAULT_LAT

	pnt = Point(lon, lat, srid=4326)
	pnt.transform(3857)
	default_lon, default_lat = pnt.coords

	def save_model(self, request, obj, form, change):
		if not change:
			obj.creator = request.user

		obj.modifier = request.user
		obj.save()


admin.site.register(Layer, BaseAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Model, BaseAdmin)

admin.site.register(LayerData, BaseAdmin)
admin.site.register(LocationData, BaseAdmin)
