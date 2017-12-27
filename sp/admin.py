from django.contrib import admin
from .models import (
	Serie,
	Package
	)

class SerieAdmin(admin.ModelAdmin):
	list_display = ('name', 'mfal', 'preference', 'ponderacion',)


class PackageAdmin(admin.ModelAdmin):
	list_display = ('name', 'mfal', 'preference',)


admin.site.register(Serie, SerieAdmin)
admin.site.register(Package, PackageAdmin)