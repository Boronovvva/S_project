from rest_framework.permissions import BasePermission

class UserPermissions(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(obj.user.pk == request.user.pk)