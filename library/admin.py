from django.contrib import admin
from . import models

admin.site.register(models.Borrow)
admin.site.register(models.Books)
admin.site.register(models.Students)
admin.site.register(models.Category)
admin.site.register(models.SubCategory)