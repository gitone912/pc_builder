from django.urls import path
from . import views

urlpatterns = [
#    user authentication
    path("", views.homepage, name="homepage"),
]