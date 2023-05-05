from django.urls import path
from .views import aboutus

urlpatterns = [
    path('', aboutus, name="aboutus"),
]
