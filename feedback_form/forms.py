from django import forms
from feedback_form.models import Feedback, Employee

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
