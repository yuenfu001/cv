from django.urls import path
from . import views

urlpatterns =[
    path("", views.index, name="home"),
    path("display_info/", views.display, name="disp"),
    path("personal_info/<str:pk>/", views.personal, name="person"),
    path("registration/", views.CreateInfo, name="register")
]