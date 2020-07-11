from django.urls import path
from . import views
from .views import ExampleModelListView, ExampleModelDetailView, ExampleModelCreateView

urlpatterns = [
    path('', ExampleModelListView.as_view(), name='index'),
    path('posts/<int:pk>/', ExampleModelDetailView.as_view(), name='view-post'),
    path('posts/new/', ExampleModelCreateView.as_view(), name='new-post'),
    path('register/', views.register, name='register'),
    path('sign-in/', views.signin, name='sign-in'),

]
