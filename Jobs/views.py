from django.shortcuts import render
from .models import Job


# Create your views here.
def home(request):
    my_job = Job.objects
    return render(request, 'Jobs/index.html', {'jobs': my_job})

