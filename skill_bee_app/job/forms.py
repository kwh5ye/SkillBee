from django import forms
from job.models import Job
from django.contrib.auth.models import User

class JobRequestForm(forms.ModelForm):
    class Meta:
      model = Job
      fields = ('description', 'category')

