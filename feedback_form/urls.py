from django.conf.urls import *

'''
    these all assume http[s]://URI/feedback_form/ as the base
'''

urlpatterns = patterns('',
    (r'^$', 'feedback_form.views.enter_feedback'),
   )
