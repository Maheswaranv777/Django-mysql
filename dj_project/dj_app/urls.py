from django.urls import path,include
from .views import *
urlpatterns=[
    path("add/",home,name="home"),
    path("show/",show,name="show"),
    path("update/<u>",update,name="update"),
    path("delete/<l>",delete,name="delete"),


]