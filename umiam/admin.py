from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from . import models


class HMCMemberAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'designation', 'hmc')
    list_filter = ('hmc',)


class AchievementAdmin(SummernoteModelAdmin):
    list_display = ('__str__',)
    summernote_fields = ('achievement_description',)


admin.site.register(models.HMCMember, HMCMemberAdmin)
admin.site.register(models.Gallery)
admin.site.register(models.Achievement, AchievementAdmin)
admin.site.register(models.QuickLinks)
admin.site.register(models.HMC)
admin.site.register(models.GalleryOverview)
admin.site.register(models.Facility)
