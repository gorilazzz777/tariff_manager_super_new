from django.contrib import admin
from .models import *


class PackageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'weight', )
    list_display_links = ('id', 'name', 'weight', )


admin.site.register(Package, PackageAdmin)
