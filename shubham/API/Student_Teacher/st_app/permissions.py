from rest_framework import permissions
from .models import User

class IsTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        user_obj =  User.objects.get(email=request.user.email)
        print(user_obj.role, 'dslkj')
        if user_obj:
            if user_obj.role == 'teacher' and user_obj.is_active:
                return True
        else:
            return False
        return False
