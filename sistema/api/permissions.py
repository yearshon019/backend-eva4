from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    """
    Admin (superuser): CRUD completo
    Operador (staff): solo lectura
    """

    message = "No tiene permisos para realizar esta acción."

    def has_permission(self, request, view):
        user = request.user

        if not user or not user.is_authenticated:
            return False

        # Métodos de solo lectura
        if request.method in SAFE_METHODS:
            return True

        # Escritura solo para admin
        return user.is_superuser
