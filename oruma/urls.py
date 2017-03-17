from django.conf.urls import url
from . views import form1view, stage_2_view, stage_3_view, application_summary,applications, landing_view


urlpatterns = [
    url(r'^$', landing_view, name='landing_view' ),
    url(r'^apply/$', form1view, name='stage1view' ),
    url(r'^applications/$', applications, name='applications' ),
    url(r'^(?P<application_number>\d+)/$', stage_2_view, name='stage_2_view'),
    url(r'^(?P<application_number>\d+)/(?P<stage_number>\d+)$', stage_3_view, name='stage_3_view'),
    url(r'^(?P<application_number>\d+)/Summary$', application_summary, name='application_summary'),

]
