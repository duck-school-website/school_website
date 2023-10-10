from django.urls import include, path
from .views import *

urlpatterns = [
    path("index/",index.as_view,name="index"),
]
