from django.contrib import admin
from .models import Applicant, Recommender, Dependend, Application, Detail, Documents, ApplicationNotes

from django.conf import settings



class DocumentAdmin(admin.ModelAdmin):
    list_display = ('application', '__str__')
    search_fields = ['application__application_number',]

admin.site.register(Documents, DocumentAdmin )

# Only allow models other than documents if debug is true
if settings.DEBUG:
    # Register your models here.
    admin.site.register(Applicant)
    admin.site.register(Recommender)
    admin.site.register(Dependend)


    class ApplicationAdmin(admin.ModelAdmin):
        list_display = ('application_number', 'status')
    admin.site.register(Application, ApplicationAdmin)



    admin.site.register(Detail)

    admin.site.register(ApplicationNotes)
