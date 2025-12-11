from rest_framework.permissions import BasePermission
from rest_framework import permissions

class SoloAdminPuedeEscribir(BasePermission):
    """
    Permite solo lectura a OPERADORES.
    Permite lectura + escritura a ADMIN.
    """

    message = "No tiene permisos para realizar esta acción."

    def has_permission(self, request, view):
        user = request.user

        # Si no está autenticado → DRF devolverá 401 automáticamente
        if not user or not user.is_authenticated:
            self.message = "Debe autenticarse para acceder a este recurso."
            return False

        # Si el usuario no tiene perfil (raro, pero seguro)
        perfil = getattr(user, "perfilusuario", None)
        if perfil is None:
            self.message = "El usuario no posee un rol válido."
            return False

        # ADMIN → acceso total
        if perfil.rol == "ADMIN":
            return True

        # OPERADOR → solo lectura
        if perfil.rol == "OPERADOR":
            solo_lectura = ["GET", "HEAD", "OPTIONS"]
            if request.method in solo_lectura:
                return True
            self.message = "Su rol OPERADOR no permite modificar datos."
            return False

        # Rol desconocido
        self.message = "Rol de usuario no reconocido."
        return False
