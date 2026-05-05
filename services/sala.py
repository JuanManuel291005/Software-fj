from modelos.servicio import Servicio
from utilidades.excepciones import ErrorServicio


class ServicioSala(Servicio):

    def calcular_costo(self, horas):
        try:
            if horas <= 0:
                raise ErrorServicio("Horas inválidas")
            return horas * 50
        except Exception as e:
            raise ErrorServicio("Error en servicio de sala") from e

    def descripcion(self):
        return "Reserva de sala por horas"
