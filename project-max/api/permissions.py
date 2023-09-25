from rest_framework import permissions

class ReadOnlyOrAdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Permite solicitudes GET a todos los usuarios
        if request.method == 'GET':
            return True
        # Restringe solicitudes POST, PUT y DELETE a administradores
        return request.user and request.user.is_staff
