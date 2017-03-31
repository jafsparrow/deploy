from django.conf.urls import url
from . views import ( form1view, stage_2_view, stage_3_view, application_summary,applications, landing_view,
                        applicantion_user_edit,
                        applicant_update_view,
                        applicant_create_view,
                        recommender_create_view,
                        recommender_update_view,
                        application_step_1,
                        application_step_2,
                        application_step_3,
                        application_step_4,
                        application_step_5
                        )


urlpatterns = [
    url(r'^$', landing_view, name='landing_view' ),
    url(r'^apply/$', form1view, name='stage1view' ),

    url(r'^(?P<application_number>\d+)/edit/$', applicantion_user_edit, name='applicantion_user_edit' ),
    url(r'^applications/$', applications, name='applications' ),
    url(r'^(?P<application_number>\d+)/$', stage_2_view, name='stage_2_view'),
    url(r'^(?P<application_number>\d+)/(?P<stage_number>\d+)$', stage_3_view, name='stage_3_view'),
    url(r'^(?P<application_number>\d+)/Summary$', application_summary, name='application_summary'),

    # Edit URLs for Applicant and Recommender
    url(r'^applicant/(?P<applicant_id>\d+)/edit$', applicant_update_view, name='applicant_update_view' ),
    url(r'^applicant/create/$',applicant_create_view, name = 'applicant_create_view' ),
    url(r'^recommender/(?P<recommender_id>\d+)/edit$', recommender_update_view, name='recommender_update_view' ),
    url(r'^recommender/create/$', recommender_create_view, name = 'recommender_create_view' ),

    # Steps
    url(r'^stage1/$', application_step_1, name='application_step_1'),
    url(r'^stage2/(?P<application_number>\d+)/$', application_step_2, name='application_step_2'),
    url(r'^stage3/(?P<application_number>\d+)/$', application_step_3, name='application_step_3'),
    url(r'^stage4/(?P<application_number>\d+)/$', application_step_4, name='application_step_4'),
    url(r'^stage5/(?P<application_number>\d+)/$', application_step_5, name='application_step_5')


]
