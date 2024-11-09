from django.db import models

from django.db import models

class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    about_me = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)  # Field for profile picture


class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    graduation_year = models.CharField(max_length=10)

class Skill(models.Model):
    name = models.CharField(max_length=50)

class Project(models.Model):
    project_name = models.CharField(max_length=100)
    description = models.TextField()
    technologies_used = models.CharField(max_length=100)

class Experience(models.Model):
    company_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    responsibilities = models.TextField()
