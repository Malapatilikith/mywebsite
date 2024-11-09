from django.urls import path
from . import views  # Import views from your app

urlpatterns = [
    path('', views.home, name='home'),  # Add a path for the homepage
]
