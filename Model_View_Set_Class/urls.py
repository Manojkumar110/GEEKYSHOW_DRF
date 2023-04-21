from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Model_View_Set_Class.views import HomeView

router = DefaultRouter()
router.register('', HomeView, basename='homeview')

urlpatterns = [
    path('', include(router.urls))
]