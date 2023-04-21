from django.urls import path, include
from View_Set_Class.views import HomeView
from rest_framework.routers import DefaultRouter

# Create Router
router = DefaultRouter()
print(' Default :',router)
print('Router Url :', router.urls)

router.register('', HomeView, basename='student')



urlpatterns = [
    path('', include(router.urls))
]
