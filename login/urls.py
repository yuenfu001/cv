from django.urls import path
from . import views
urlpatterns = [
    path("", views.anything,name="any")
]