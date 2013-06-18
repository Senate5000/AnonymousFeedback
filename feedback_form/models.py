from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Feedback(models.Model):
    name = models.ForeignKey(Employee)
    timeframe_start = models.DateField(auto_now=False)
    timeframe_stop = models.DateField(auto_now=False, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    feedback = models.TextField(blank = False, null = False)