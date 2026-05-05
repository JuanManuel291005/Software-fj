from modelos.servicio import Servicio
from utilidades.excepciones import ErrorServicio


class ServicioEquipo(Servicio):

    def calcular_costo(self, dias):
        try:
            if dias <= 0:
                raise ErrorServicio("Días inválidos")
            return dias * 30
        except Exception as e:
            raise ErrorServicio("Error en servicio de equipo") from e

    def descripcion(self):
        return "Alquiler de equipos por días"
