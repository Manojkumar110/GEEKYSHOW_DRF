from django.urls import path, include
from SessionBase_AuthenthicationPermission.views import HomeView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', HomeView, basename='sessionhomeview')
urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]