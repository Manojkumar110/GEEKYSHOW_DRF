from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Basic_AuthenticationPermissions.views import BasicAuthView

router = DefaultRouter()
router.register('', BasicAuthView, basename='basicauthentication')

urlpatterns = [
    path('', include(router.urls))
]
