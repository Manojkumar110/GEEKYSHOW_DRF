from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),

    #1.----------------Serializer------------------------
    # path('', include('SerializerApp.urls')),

    #2.----------Function BaseView Serialiazer-----------
    # path('', include('FunctionBaseSerializer.urls')),

    #3.----------------Validator------------------------
    # path('', include('ValidatorApp.urls')),

    #4.-------------Model Serializer--------------------
    # path('', include('ModelSerializer.urls')),

    #5.--------------Function Base Api View-------------
    # path('', include('FunctionBaseApiView.urls')),


    #6.----------Class Base  Api View  -------------
    # path('', include('Class_Base_Api_View.urls')),

    #7.--------Generic Api View Model Mixin-------------
    # path('', include('Generic_Api_View_Model_Mixin.urls')),

    # 8.---------------View Set Class--------------------
    # path('', include('View_Set_Class.urls')),

    # 9.--------------Model View Set Class---------------
    # path('', include('Model_View_Set_Class.urls')),

    # 10.----------Basic_AuthenticationPermissions-------
    # path('', include('Basic_AuthenticationPermissions.urls')),

    # 11. ---------SessionBase_AuthenthicationPermission-----
    # path('', include('SessionBase_AuthenthicationPermission.urls')),

    # 12. -----------------Custome_Permission---------------
    # path('', include('Custome_Permission.urls')),

    # 13.-------------Function Base Auth Permission-----------
    path('', include('FunctionBaseAuthPermission.urls'))
]
