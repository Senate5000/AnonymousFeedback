from django.contrib import admin
from feedback_form.models import Feedback, Employee

class FeedbackAdmin(admin.ModelAdmin):
    readonly_fields = ['timestamp']

admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Employee)
