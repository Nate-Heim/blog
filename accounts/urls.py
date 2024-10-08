# accounts/urls.py
# Nate Heim

# adding needed links

from django.urls import path
from .views import SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
]
