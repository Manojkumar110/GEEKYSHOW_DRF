from django.urls import path
from ModelSerializer.views import HomeView

urlpatterns = [
    path('', HomeView),
    path('<int:pk>', HomeView)
]