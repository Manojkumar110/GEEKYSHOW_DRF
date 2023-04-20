from django.urls import path
from FunctionBaseSerializer.views import HomeView

urlpatterns = [
    path('', HomeView, name=''),
    path('<int:pk>', HomeView, name='')
]