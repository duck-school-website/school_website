from django.urls import include, path
from .views import *


urlpatterns = [
    path("index/",index.as_view(),name="index"),
    path("my_class/",my_class.as_view(),name="class"),
]
