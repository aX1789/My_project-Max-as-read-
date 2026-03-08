# from django.shortcuts import render
from django.views.generic import TemplateView 
# Create your views here.
class Mainpage(TemplateView):
    template_name = "mainpage/home.html"

