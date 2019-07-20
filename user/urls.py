from django.urls import path
from .views import UserLoginView, UserRegistrationView

urlpatterns = [
    path('v1/login', UserLoginView.as_view(), name='login'),
    path('v1/register', UserRegistrationView.as_view(), name='register')
]