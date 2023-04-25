from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Custome_Permission.views import HomeView
router = DefaultRouter()
router.register('', HomeView, basename='homeview')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]