from django.urls import path
from . import views

urlpatterns  =[
    path('school-info/',views.get_school_info),
]