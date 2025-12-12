from rest_framework.response import Response
from rest_framework import status as st

class StandardResponseMixin:
    """
    Envuelve respuestas exitosas en un formato estándar:
    {
      "codigo": 201,
      "mensaje": "...",
      "data": {...}
    }
    """

    success_messages = {
        "list": "Listado obtenido correctamente.",
        "retrieve": "Registro obtenido correctamente.",
        "create": "Registro creado correctamente.",
        "update": "Registro actualizado correctamente.",
        "partial_update": "Registro actualizado correctamente.",
        "destroy": "Registro eliminado correctamente.",
    }

    def _ok(self, *, http_status, mensaje, data=None):
        payload = {"codigo": http_status, "mensaje": mensaje}
        if data is not None:
            payload["data"] = data
        return Response(payload, status=http_status)

    # GET / (lista)
    def list(self, request, *args, **kwargs):
        resp = super().list(request, *args, **kwargs)
        return self._ok(
            http_status=st.HTTP_200_OK,
            mensaje=self.success_messages["list"],
            data=resp.data
        )

    # GET /{id}/
    def retrieve(self, request, *args, **kwargs):
        resp = super().retrieve(request, *args, **kwargs)
        return self._ok(
            http_status=st.HTTP_200_OK,
            mensaje=self.success_messages["retrieve"],
            data=resp.data
        )

    # POST /
    def create(self, request, *args, **kwargs):
        resp = super().create(request, *args, **kwargs)  # resp.status_code será 201
        return self._ok(
            http_status=st.HTTP_201_CREATED,
            mensaje=self.success_messages["create"],
            data=resp.data
        )

    # PUT /{id}/
    def update(self, request, *args, **kwargs):
        resp = super().update(request, *args, **kwargs)
        return self._ok(
            http_status=st.HTTP_200_OK,
            mensaje=self.success_messages["update"],
            data=resp.data
        )

    # PATCH /{id}/
    def partial_update(self, request, *args, **kwargs):
        resp = super().partial_update(request, *args, **kwargs)
        return self._ok(
            http_status=st.HTTP_200_OK,
            mensaje=self.success_messages["partial_update"],
            data=resp.data
        )

    # DELETE /{id}/
    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return self._ok(
            http_status=st.HTTP_200_OK,
            mensaje=self.success_messages["destroy"],
            data=None
        )
