from abc import ABC, abstractmethod
from mediador import MediadorChat

class Usuario(ABC):
    """Clase base para los componentes que se comunican."""
    
    def __init__(self, mediador: MediadorChat, nombre: str) -> None:
        self.mediador = mediador
        self.nombre = nombre

    @abstractmethod
    def enviar(self, mensaje: str) -> None:
        pass

    @abstractmethod
    def recibir(self, mensaje: str, remitente_nombre: str) -> None:
        pass


class UsuarioConcreto(Usuario):
    """Implementación de un usuario específico de la sala de chat."""
    
    def enviar(self, mensaje: str) -> None:
        print(f"\n{self.nombre} envía: '{mensaje}'")
        # El usuario delega completamente el enrutamiento al mediador
        self.mediador.enviar_mensaje(mensaje, self)

    def recibir(self, mensaje: str, remitente_nombre: str) -> None:
        print(f"  -> {self.nombre} recibe de {remitente_nombre}: '{mensaje}'")