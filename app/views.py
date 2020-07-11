from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import ExampleModel

from django.http import HttpResponse

# Create your views here.


class ExampleModelListView(ListView):
    model = ExampleModel
    template_name = 'templates/index.html'
    ordering = ["-when_posted"]


class ExampleModelDetailView(DetailView):
    model = ExampleModel
    template_name = 'templates/post.html'


class ExampleModelCreateView(CreateView):
    model = ExampleModel
    fields = ['title', 'content']
    template_name = 'templates/newpost.html'


def register(request):
    return HttpResponse("Register Page")


def signin(request):
    return HttpResponse("Sign In Page")
