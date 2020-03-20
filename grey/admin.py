# Purpose of this file:
# This file exists to configure Django's admin interface

from django.contrib import admin
# Always import your models before using them
from .models import FileClass, FileItem

# Register your models here to have them show up in the admin interface

admin.site.register(FileClass)
admin.site.register(FileItem)
