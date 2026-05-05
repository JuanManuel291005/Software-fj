class ErrorSistema(Exception):
    """Clase base para errores del sistema"""
    pass


class ErrorCliente(ErrorSistema):
    """Errores relacionados con clientes"""
    pass


class ErrorServicio(ErrorSistema):
    """Errores relacionados con servicios"""
    pass


class ErrorReserva(ErrorSistema):
    """Errores relacionados con reservas"""
    pass
