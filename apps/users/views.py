from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import redirect
from django.contrib.auth import logout, login
from apps.users.serializers import UserSerializer, UserRegisterSerializer
from apps.users.permissions import UserPermissions
from apps.users.models import User

class UserAPI(GenericViewSet,
              mixins.ListModelMixin,
              mixins.RetrieveModelMixin,
              mixins.CreateModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return UserRegisterSerializer
        return UserSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.request.method in ('DELETE', 'PUT', 'PATCH'):
            return [UserPermissions()]
        return [IsAuthenticated()]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

def logout_user(request):
    logout(request)
    return redirect('api/')  
