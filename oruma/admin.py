from django.contrib import admin
from .models import Applicant, Recommender, Dependend, Application, Detail, Documents
# Register your models here.
admin.site.register(Applicant)
admin.site.register(Recommender)
admin.site.register(Dependend)
admin.site.register(Application)
admin.site.register(Detail)
admin.site.register(Documents)
