from django.urls import path
from ValidatorApp.views import HomeView


urlpatterns = [
    path('', HomeView)
]