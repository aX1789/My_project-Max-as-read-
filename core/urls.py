from django.urls import path
from .views import Mainpage

urlpatterns = [
    path("", Mainpage.as_view(), name="home"),
]