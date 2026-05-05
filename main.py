from models.cliente import Cliente
from models.reserva import Reserva

from services.sala import ServicioSala
from services.equipo import ServicioEquipo
from services.asesoria import ServicioAsesoria

from utils.logger import registrar_error


def ejecutar_sistema():
    clientes = []
    reservas = []

    # ================== CLIENTES ==================
    try:
        clientes.append(Cliente("Juan", "juan@mail.com", "12345"))
        clientes.append(Cliente("Ana", "ana@mail.com", "67890"))

        # Cliente inválido
        clientes.append(Cliente("", "correo_mal", "abc"))

    except Exception as e:
        registrar_error(e)

    # ================== SERVICIOS ==================
    sala = ServicioSala()
    equipo = ServicioEquipo()
    asesoria = ServicioAsesoria()

    servicios = [sala, equipo, asesoria]

    # ================== RESERVAS ==================
    for i in range(10):
        try:
            cliente = clientes[0]
            servicio = servicios[i % 3]

            # Duración inválida en algunos casos
            duracion = i  # cuando i = 0 → error

            reserva = Reserva(cliente, servicio, duracion)
            reservas.append(reserva)

            reserva.confirmar()

            total = reserva.procesar()
            print(f"Reserva {i} - Total: {total}")

        except Exception as e:
            registrar_error(e)

    print("\nSistema ejecutado correctamente sin detenerse.")


if __name__ == "__main__":
    ejecutar_sistema()
