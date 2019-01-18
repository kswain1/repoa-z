from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.AthleteProfile)
admin.site.register(models.AthleteFeedItem)
admin.site.register(models.AthleteEMGDataItem)
admin.site.register(models.Player)
admin.site.register(models.Composite)
admin.site.register(models.Session)
admin.site.register(models.Injury)
admin.site.register(models.SessionLog)