from rest_framework.permissions import BasePermission


class MyPermission(BasePermission):

    def has_permission(self, request, view):
        print(request.user.get('user_type', None))
        if int(request.user.get('user_type', None)) == 1:
            return True
        return False
