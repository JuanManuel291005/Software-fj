from models.servicio import Servicio
from utils.excepciones import ErrorServicio


class ServicioAsesoria(Servicio):

    def calcular_costo(self, horas):
        try:
            if horas <= 0:
                raise ErrorServicio("Horas inválidas")
            return horas * 100
        except Exception as e:
            raise ErrorServicio("Error en asesoría") from e

    def descripcion(self):
        return "Asesoría especializada por horas"
