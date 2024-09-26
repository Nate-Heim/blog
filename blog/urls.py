# Nate Heim
# blog/urls.py

from django.urls import path
from .views import post_list, post_detail  # added post_detail

urlpatterns = [
    path("post/<int:pk>/", post_detail, name="post_detail"),  # added
    path("", post_list, name="home"),
]
