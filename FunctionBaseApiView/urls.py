from django.urls import path
from FunctionBaseApiView.views import HomeView

urlpatterns = [
    path('', HomeView),
    path('<int:pk>', HomeView),
]