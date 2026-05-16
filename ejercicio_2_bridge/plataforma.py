from abc import ABC, abstractmethod

# Principio de separación de responsabilidades: Esta jerarquía solo se preocupa por el medio por el que se presenta
class Plataforma(ABC):
    """Interfaz Implementadora."""
    
    @abstractmethod
    def mostrar(self, titulo: str, contenido: str) -> None:
        pass

# Escalabilidad: Crear una nueva clase sin tocar el código de las Notificaciones.
class PlataformaWeb(Plataforma):
    def mostrar(self, titulo: str, contenido: str) -> None:
        print(f"[WEB UI] {titulo}")
        print(f"   Contenido HTML: <p>{contenido}</p>")

class PlataformaMovil(Plataforma):
    def mostrar(self, titulo: str, contenido: str) -> None:
        print(f"[PUSH MÓVIL] {titulo}")
        print(f"   Payload: {{ 'body': '{contenido}' }}")

class PlataformaEscritorio(Plataforma):
    def mostrar(self, titulo: str, contenido: str) -> None:
        print(f"[NATIVO ESCRITORIO] Ventana emergente: {titulo}")
        print(f"   Texto: {contenido}")