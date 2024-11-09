from django import forms
from .models import PersonalInfo, Education, Skill, Project, Experience

class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = '__all__'
