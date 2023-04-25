from django.urls import path
from FunctionBaseAuthPermission.views import HomeView1, HomeView2


urlpatterns = [
    path('homeview1',HomeView1.as_view(), name='homepage1'),
    path('homeview2',HomeView2.as_view(), name='homepage2'),
]