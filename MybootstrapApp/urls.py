from django.urls import path
from MybootstrapApp import views

urlpatterns=[
    path('',views.home,name='my_name'),


]