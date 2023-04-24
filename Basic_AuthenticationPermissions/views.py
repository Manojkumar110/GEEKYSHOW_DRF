from rest_framework import viewsets
from Basic_AuthenticationPermissions.models import Student
from Basic_AuthenticationPermissions.serializers import StudentSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# Create your views here.

# note : It is Not Implement by DRF


class BasicAuthView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes = [BasicAuthentication] 
    # permission_classes = [IsAuthenticated]
    # override process      
    permission_classes = [IsAdminUser]


# Basic Authentication:-
# 1. Basic Authentication
# 2. Session Authentication
# 3. Token Authentication
# 4. Remote User
# 5. Custom Authentication

# Permission Classes:-
# 1. AllowAny           2. IsAuthenticate     3. IsAdminUser

# 4. IsAuthenticateOrReadOnly       5. DjangoModelPermission

# 7. DjangoModelPermissionOrAnonReadOnly

# 8. DjangoObjectPermission

# 9. CustomePermission
