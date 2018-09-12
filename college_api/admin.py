from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.AthleteProfile)
admin.site.register(models.AthleteFeedItem)
admin.site.register(models.AthleteEMGDataItem)