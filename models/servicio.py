from abc import ABC, abstractmethod
from utilidades.excepciones import ErrorServicio


class Servicio(ABC):

    @abstractmethod
    def calcular_costo(self, duracion):
        """Debe ser implementado por cada servicio"""
        pass

    @abstractmethod
    def descripcion(self):
        """Describe el servicio"""
        pass

    # Método con "sobrecarga simulada"
    def calcular_costo_con_extra(self, duracion, impuesto=0, descuento=0):
        try:
            base = self.calcular_costo(duracion)
            total = base + (base * impuesto) - descuento
            return total
        except Exception as e:
            raise ErrorServicio("Error al calcular costo") from e
