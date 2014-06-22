from django.contrib import admin
from models import *


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('admin_image_view', 'name')
    list_select_related = True

admin.site.register(Photo, PhotoAdmin)
