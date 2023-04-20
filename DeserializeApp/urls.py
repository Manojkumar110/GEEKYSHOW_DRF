from django.urls import path
from DeserializeApp.views import HomeView


urlpatterns = [
    path('', HomeView, name='homepage')
]