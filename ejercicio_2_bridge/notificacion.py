from abc import ABC, abstractmethod
from plataforma import Plataforma

# Reducción de clases.
# No necesitamos clases como NotificacionMensajeWeb o NotificacionAlertaMovil.
class Notificacion(ABC):
    """Clase Abstracción Base."""
    
    def __init__(self, plataforma: Plataforma):
        self._plataforma = plataforma  # Referencia al implementador - El Puente

    # Flexibilidad en tiempo de ejecución. 
    # Permite inyectar una nueva plataforma a un objeto ya instanciado en plena ejecución.
    def cambiar_plataforma(self, nueva_plataforma: Plataforma) -> None:
        self._plataforma = nueva_plataforma

    @abstractmethod
    def enviar(self, mensaje: str) -> None:
        pass


class NotificacionMensaje(Notificacion):
    """Abstracción Refinada para un tipo específico de notificación."""
    
    def enviar(self, mensaje: str) -> None:
        titulo = "Nuevo Mensaje"
        contenido_formateado = f"Universidad de la Sabana informa: {mensaje}"
        # Se delega la presentación a la plataforma inyectada
        self._plataforma.mostrar(titulo, contenido_formateado)


class NotificacionAlerta(Notificacion):
    """Abstracción Refinada para otro tipo de notificación."""
    
    def enviar(self, mensaje: str) -> None:
        titulo = "¡ALERTA DE SISTEMA!"
        contenido_formateado = f"OJITO: {mensaje.upper()}"
        self._plataforma.mostrar(titulo, contenido_formateado)