from dataclasses import dataclass
from typing import Optional

# Inmutabilidad: Cuando el objeto se crea, no se puede modificar. 
# Flexibilidad: Los atributos opcionales si pueden ser None.
@dataclass(frozen=True)
class Automovil:
    """
    Clase Producto. Será inmutable gracias al parámetro frozen=True.
    """
    motor: str
    color: str
    llantas: str
    sistema_sonido: Optional[str] = None
    interiores: Optional[str] = None
    techo_solar: bool = False
    navegacion_gps: bool = False

    def __str__(self) -> str:
        partes = [f"Motor: {self.motor}", f"Color: {self.color}", f"Llantas: {self.llantas}"]
        if self.sistema_sonido: partes.append(f"Sonido: {self.sistema_sonido}")
        if self.interiores: partes.append(f"Interiores: {self.interiores}")
        partes.append(f"Techo Solar: {'Sí' if self.techo_solar else 'No'}")
        partes.append(f"GPS: {'Sí' if self.navegacion_gps else 'No'}")
        
        return " | ".join(partes)