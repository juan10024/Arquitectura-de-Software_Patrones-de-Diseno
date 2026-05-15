from abc import ABC, abstractmethod
from typing import Optional
from producto import Automovil

# Legibilidad y Claridad
class ConstructorAutomovil(ABC):
    """Interfaz abstracta del Builder. El Builder acumula el estado y luego crea el Automovil"""
    
    @abstractmethod
    def reset(self) -> None: pass
    
    @abstractmethod
    def set_motor(self, motor: str) -> 'ConstructorAutomovil': pass
    
    @abstractmethod
    def set_color(self, color: str) -> 'ConstructorAutomovil': pass
    
    @abstractmethod
    def set_llantas(self, llantas: str) -> 'ConstructorAutomovil': pass
    
    @abstractmethod
    def set_sistema_sonido(self, sistema: str) -> 'ConstructorAutomovil': pass
    
    @abstractmethod
    def set_interiores(self, interiores: str) -> 'ConstructorAutomovil': pass
    
    @abstractmethod
    def set_techo_solar(self, tiene_techo: bool) -> 'ConstructorAutomovil': pass
    
    @abstractmethod
    def set_gps(self, tiene_gps: bool) -> 'ConstructorAutomovil': pass
    
    @abstractmethod
    def construir(self) -> Automovil: pass


class ConstructorAutomovilConcreto(ConstructorAutomovil):
    """Implementación específica que ensambla el automóvil paso a paso."""
    
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        # Estado temporal interno antes de la construcción
        self._motor: str = ""
        self._color: str = ""
        self._llantas: str = ""
        self._sistema_sonido: Optional[str] = None
        self._interiores: Optional[str] = None
        self._techo_solar: bool = False
        self._navegacion_gps: bool = False

    # Retornar 'self' porque permite encadenar métodos
    def set_motor(self, motor: str) -> 'ConstructorAutomovilConcreto':
        self._motor = motor
        return self

    def set_color(self, color: str) -> 'ConstructorAutomovilConcreto':
        self._color = color
        return self

    def set_llantas(self, llantas: str) -> 'ConstructorAutomovilConcreto':
        self._llantas = llantas
        return self

    def set_sistema_sonido(self, sistema: str) -> 'ConstructorAutomovilConcreto':
        self._sistema_sonido = sistema
        return self

    def set_interiores(self, interiores: str) -> 'ConstructorAutomovilConcreto':
        self._interiores = interiores
        return self

    def set_techo_solar(self, tiene_techo: bool) -> 'ConstructorAutomovilConcreto':
        self._techo_solar = tiene_techo
        return self

    def set_gps(self, tiene_gps: bool) -> 'ConstructorAutomovilConcreto':
        self._navegacion_gps = tiene_gps
        return self

    def construir(self) -> Automovil:
        """Instancia y retorna el producto final inmutable."""
        if not self._motor or not self._color or not self._llantas:
            raise ValueError("El automóvil debe tener al menos motor, color y llantas.")
            
        automovil = Automovil(
            motor=self._motor,
            color=self._color,
            llantas=self._llantas,
            sistema_sonido=self._sistema_sonido,
            interiores=self._interiores,
            techo_solar=self._techo_solar,
            navegacion_gps=self._navegacion_gps
        )
        self.reset() # Queda el builder listo para el siguiente vehículo
        return automovil