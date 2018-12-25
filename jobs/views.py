from django.shortcuts import render
from .models import Job
# Create your views here.
def index(request):
	jobs = Job.objects
	context = {
       'jobs': jobs
	}
	return render(request , 'jobs/home.html',context)
