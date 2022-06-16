from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import ExampleModelListView, ExampleModelDetailView, ExampleModelCreateView

urlpatterns = [
    path('', ExampleModelListView.as_view(paginate_by=1), name='home'),
    path('posts/<int:pk>/', ExampleModelDetailView.as_view(), name='view-post'),
    path('posts/new/', ExampleModelCreateView.as_view(), name='new-post'),
    path('register/', views.register, name='register'),
    path('sign-in/', auth_views.LoginView.as_view(template_name='templates/login.html'), name='sign-in'),
    path('sign-out/', auth_views.LogoutView.as_view(
        template_name='templates/logout.html'), name='sign-out'),
    path('update-profile/', views.profile, name="update-profile")
]
