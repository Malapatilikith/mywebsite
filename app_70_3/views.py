from django.shortcuts import render
from .models import PersonalInfo

def home(request):
    # Retrieve the first PersonalInfo object (adjust logic if you have multiple entries)
    personal_info = PersonalInfo.objects.first()
    return render(request, 'app_70_3/resume.html', {'personal_info': personal_info})
