from rest_framework.permissions import BasePermission, SAFE_METHODS

class SoloAdminPuedeEscribir(BasePermission):
    """
    - Si NO está autenticado: no pasa.
    - Si es GET/HEAD/OPTIONS: pasa siempre.
    - Si es POST/PUT/PATCH/DELETE: solo si el rol es ADMIN.
    """

    def has_permission(self, request, view):
        user = request.user

        if not user or not user.is_authenticated:
            return False

        if request.method in SAFE_METHODS:
            return True

        perfil = getattr(user, 'perfil', None)
        if perfil and perfil.rol == 'ADMIN':
            return True

        return False
