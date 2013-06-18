from django.shortcuts import render_to_response
from feedback_form.forms import FeedbackForm 
from feedback_form.models import Feedback
from django.template import RequestContext


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