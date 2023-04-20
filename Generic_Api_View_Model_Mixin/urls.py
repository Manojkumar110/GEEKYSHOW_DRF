from django.urls import path
from Generic_Api_View_Model_Mixin.views import HomeView_List

urlpatterns = [
    path('', HomeView_List.as_view())
]