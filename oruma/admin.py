from django.contrib import admin
from .models import Applicant, Recommender, Dependend, Application, Detail, Documents, ApplicationNotes
# Register your models here.
admin.site.register(Applicant)
admin.site.register(Recommender)
admin.site.register(Dependend)


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('application_number', 'status')
admin.site.register(Application, ApplicationAdmin)



admin.site.register(Detail)
admin.site.register(Documents)
admin.site.register(ApplicationNotes)
