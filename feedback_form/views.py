from django.shortcuts import render_to_response
from feedback_form.forms import FeedbackForm, EmployeeForm
from feedback_form.models import Feedback, Employee
from django.template import RequestContext
from django.contrib.auth.decorators import permission_required


# Create your views here.

def enter_feedback(request):
    if request.method == 'POST':
        feedback = Feedback()
        form = FeedbackForm(request.POST, instance=feedback)

        if form.is_valid():
            try:
                feedback = form.save()
            except Exception, e:
                print e
    else:
        form = FeedbackForm()

    return render_to_response('feedback_form/feedback.html', {'form': form}, context_instance=RequestContext(request))


def new_employee(request):
    if request.method == 'POST':
        employee = Employee()
        form = EmployeeForm(request.POST, instance=employee)

        if form.is_valid():
            try:
                employee = form.save()
            except Exception, e:
                print e
    else:
        form = EmployeeForm()

    return render_to_response('feedback_form/new_employee.html', {'form': form}, context_instance=RequestContext(request))

@permission_required('feedback_form.can_delete_feedback', login_url='/admin/')
def view_feedback(request):
    feedback = Feedback.objects.all()
    employees = Employee.objects.all()

    return render_to_response('feedback_form/view_feedback.html', {'feedback': feedback, 'employees': employees}, context_instance=RequestContext(request))