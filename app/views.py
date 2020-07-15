from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView
from .models import ExampleModel
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

# Create your views here.


def main(request):
    return redirect("home")


class ExampleModelListView(ListView):
    model = ExampleModel
    template_name = 'templates/home.html'
    ordering = ["-when_posted"]


class ExampleModelDetailView(DetailView):
    model = ExampleModel
    template_name = 'templates/post.html'


class ExampleModelCreateView(CreateView):
    model = ExampleModel
    fields = ['title', 'content']
    template_name = 'templates/newpost.html'


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f"Account for {username} was created successfully!")
            return redirect("sign-in")

    else:
        form = UserRegistrationForm()

    return render(request, 'templates/register.html', {'form': form})


def signin(request):
    return HttpResponse("Sign In Page")


@login_required
def profile(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(
                request, "Your account has been updated!")
            return redirect("home")

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'templates/profile.html', {'userform': user_form, 'imageupload': profile_form})
