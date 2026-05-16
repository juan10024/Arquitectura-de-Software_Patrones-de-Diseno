from plataforma import PlataformaWeb, PlataformaMovil, PlataformaEscritorio
from notificacion import NotificacionMensaje, NotificacionAlerta

def main():
    # Instanciamos las implementaciones concretas
    web = PlataformaWeb()
    movil = PlataformaMovil()
    desktop = PlataformaEscritorio()

    print("--- Prueba 1: Mensaje en Web ---")
    notificacion_normal = NotificacionMensaje(web)
    notificacion_normal.enviar("Debes pagar tu matrícula o si no te echamos")

    print("\n--- Prueba 2: Alerta Crítica en Escritorio ---")
    alerta_sistema = NotificacionAlerta(desktop)
    alerta_sistema.enviar("Uso de CPU al 99%")

    print("\n--- Prueba 3: Flexibilidad en tiempo de ejecución ---")
    # El usuario minimiza la app de escritorio y se va. Entonces dinámicamente cambia la plataforma a móvil sin destruir la notificación.
    alerta_sistema.cambiar_plataforma(movil)
    alerta_sistema.enviar("Uso de CPU se mantiene elevado")

if __name__ == "__main__":
    main()