from django.urls import path
from . import views

urlpatterns =[
    path("", views.hmmm, name="home")
]