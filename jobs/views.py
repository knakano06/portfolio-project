from django.shortcuts import render

# access item in the data base
from .models import Job

# Create your views here.
def home(request):
    # get the job objects here and pass it back using this render
    jobs = Job.objects # list of jobs
    # pass in the dictionary of jobs 
    return render(request, 'jobs/home.html', {'jobs': jobs})
