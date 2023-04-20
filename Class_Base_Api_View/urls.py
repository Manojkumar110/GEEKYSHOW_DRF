from django.urls import path
from Class_Base_Api_View.views import HomeView

urlpatterns = [
    path('', HomeView.as_view()),
    path('<int:pk>', HomeView.as_view())
]