from django.conf.urls import *

'''
    these all assume http[s]://URI/feedback_form/ as the base
'''

urlpatterns = patterns('',
    (r'view_feedback', 'feedback_form.views.view_feedback'),
    (r'feedback', 'feedback_form.views.enter_feedback'),
    (r'new_employee', 'feedback_form.views.new_employee'),
   )
