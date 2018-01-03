from django.contrib import admin
from .models import (
	Serie,
	Package
	)

class SerieAdmin(admin.ModelAdmin):
	list_display = ('name', 'mfal', 'take_rate', 'ponderacion',)


class PackageAdmin(admin.ModelAdmin):
	list_display = ('name', 'mfal', 'take_rate',)


admin.site.register(Serie, SerieAdmin)
admin.site.register(Package, PackageAdmin)