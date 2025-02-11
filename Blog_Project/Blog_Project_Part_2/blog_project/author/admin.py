from django.contrib import admin
from . import models # . means import all from models

# Register your models here.

admin.site.register(models.Author)
##admin.site.register(models.Profile) Author model ta admin panel a show korbe
