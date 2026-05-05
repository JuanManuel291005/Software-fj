from utils.excepciones import ErrorReserva
from utils.logger import registrar_error


class Reserva:

    def __init__(self, cliente, servicio, duracion):
        try:
            if duracion <= 0:
                raise ErrorReserva("Duración inválida")

            self.cliente = cliente
            self.servicio = servicio
            self.duracion = duracion
            self.estado = "pendiente"

        except Exception as e:
            registrar_error(e)
            raise ErrorReserva("Error al crear reserva") from e

    def confirmar(self):
        try:
            if self.estado != "pendiente":
                raise ErrorReserva("No se puede confirmar una reserva en este estado")

            self.estado = "confirmada"

        except Exception as e:
            registrar_error(e)

    def cancelar(self):
        try:
            if self.estado == "cancelada":
                raise ErrorReserva("La reserva ya está cancelada")

            self.estado = "cancelada"

        except Exception as e:
            registrar_error(e)

    def procesar(self):
        try:
            costo = self.servicio.calcular_costo(self.duracion)

        except Exception as e:
            registrar_error(e)
            raise ErrorReserva("Error al procesar la reserva") from e

        else:
            return costo

        finally:
            print("Intento de procesamiento realizado")
