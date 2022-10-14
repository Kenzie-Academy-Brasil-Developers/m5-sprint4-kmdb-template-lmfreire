from rest_framework import permissions


class IsAdminOrCritic(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        
        if request.user.is_superuser or request.user.is_critic:
            return True
        
        return False

class IsAdminOrCriticDetail(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        
        if request.user.is_superuser or request.user.id == obj[0].users.id and request.user.is_critic:
            return True
        
        return False