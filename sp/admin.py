from django.contrib import admin
from .models import (
	Serie,
	Package,
	MFAL,
	)


class MFALAdmin(admin.ModelAdmin):
	list_display = ('name', 'mfal_code',)


class SerieAdmin(admin.ModelAdmin):
	list_display = ('name', 'take_rate', 'ponderacion',)


class PackageAdmin(admin.ModelAdmin):
	list_display = ('name', 'take_rate',)


admin.site.register(Serie, SerieAdmin)
admin.site.register(Package, PackageAdmin)
admin.site.register(MFAL, MFALAdmin)