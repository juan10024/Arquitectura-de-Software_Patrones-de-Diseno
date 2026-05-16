from abc import ABC, abstractmethod

# Para evitar importaciones circulares en el tipado, usamos TYPE_CHECKING
from typing import List, TYPE_CHECKING
if TYPE_CHECKING:
    from usuario import Usuario

# Mejor organización: Toda la lógica de cómo se distribuyen los mensajes está centralizada aquí.
class MediadorChat(ABC):
    """Interfaz del Mediador."""
    
    @abstractmethod
    def registrar_usuario(self, usuario: 'Usuario') -> None:
        pass

    @abstractmethod
    def enviar_mensaje(self, mensaje: str, remitente: 'Usuario') -> None:
        pass


class SalaChatMediador(MediadorChat):
    """Implementación concreta del Mediador (La Sala de Chat)."""
    
    def __init__(self):
        self._usuarios: List['Usuario'] = []

    # Facilita el mantenimiento: Agregar o eliminar usuarios ocurre solo en esta lista del mediador.
    def registrar_usuario(self, usuario: 'Usuario') -> None:
        if usuario not in self._usuarios:
            self._usuarios.append(usuario)
            print(f"[Sistema] {usuario.nombre} se ha unido a la sala.")

    def eliminar_usuario(self, usuario: 'Usuario') -> None:
        if usuario in self._usuarios:
            self._usuarios.remove(usuario)
            print(f"[Sistema] {usuario.nombre} ha abandonado la sala.")

    # Reduce la complejidad: Evitamos la red enmarañada. El mediador recibe el mensaje y lo distribuye
    def enviar_mensaje(self, mensaje: str, remitente: 'Usuario') -> None:
        for usuario in self._usuarios:
            if usuario != remitente:
                usuario.recibir(mensaje, remitente.nombre)