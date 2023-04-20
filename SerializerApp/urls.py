from django.urls import path
from SerializerApp.views import HomeView

urlpatterns = [
    path('', HomeView, name='')
]