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
                        application_step_5,
                        submittion_review,
                        app_submit,
                        app_review,
                        app_review,
                        app_approve,
                        app_reject,
                        review_view
                        )


urlpatterns = [
    url(r'^$', landing_view, name='landing_view' ),
    # Edit URLs for Applicant and Recommender
    url(r'^applicant/(?P<applicant_id>\d+)/edit$', applicant_update_view, name='applicant_update_view' ),
    url(r'^applicant/create/$',applicant_create_view, name = 'applicant_create_view' ),
    url(r'^recommender/(?P<recommender_id>\d+)/edit$', recommender_update_view, name='recommender_update_view' ),
    url(r'^recommender/create/$', recommender_create_view, name = 'recommender_create_view' ),
    url(r'^applications/$', applications, name='applications' ),
    # Steps
    url(r'^stage1/$', application_step_1, name='application_step_1'),
    url(r'^stage2/(?P<application_number>\d+)/$', application_step_2, name='application_step_2'),
    url(r'^stage3/(?P<application_number>\d+)/$', application_step_3, name='application_step_3'),
    url(r'^stage4/(?P<application_number>\d+)/$', application_step_4, name='application_step_4'),
    url(r'^stage5/(?P<application_number>\d+)/$', application_step_5, name='application_step_5'),
    url(r'^review/(?P<application_number>\d+)/$', review_view, name='review_view'),
    url(r'^submission/(?P<application_number>\d+)/$', submittion_review, name='submittion_review'),


    # URLs for App submissio process
    url(r'^(?P<application_number>\d+)/submit$', app_submit, name='app_submit'),
    url(r'^(?P<application_number>\d+)/review$', app_review, name='app_review'),
    url(r'^(?P<application_number>\d+)/reject$', app_reject, name='app_reject'),
    url(r'^(?P<application_number>\d+)/approve$', app_approve, name='app_approve'),



]
