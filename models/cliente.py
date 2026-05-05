from models.entidad import Entidad
from utils.excepciones import ErrorCliente
from utils.logger import registrar_error


class Cliente(Entidad):
    def __init__(self, nombre, correo, telefono):
        try:
            if not nombre:
                raise ErrorCliente("Nombre inválido")

            if "@" not in correo:
                raise ErrorCliente("Correo inválido")

            if not telefono.isdigit():
                raise ErrorCliente("Teléfono inválido")

            self.__nombre = nombre
            self.__correo = correo
            self.__telefono = telefono

        except Exception as e:
            registrar_error(e)
            raise ErrorCliente("Error al crear cliente") from e

    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo

    def get_telefono(self):
        return self.__telefono

    # Setter con validación
    def set_correo(self, correo):
        try:
            if "@" not in correo:
                raise ErrorCliente("Correo inválido")
            self.__correo = correo
        except Exception as e:
            registrar_error(e)

    # Método requerido por la clase abstracta
    def mostrar_info(self):
        return f"Cliente: {self.__nombre}, Correo: {self.__correo}"
