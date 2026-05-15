from builder import ConstructorAutomovil

# Construcción separada de Representación
class DirectorAutomovil:
    """
    Orquesta el proceso de construcción para modelos predefinidos.
    Entonces aísla al cliente de los detalles de construcción de versiones comunes  
    """
    
    def __init__(self, constructor: ConstructorAutomovil):
        self._constructor = constructor

    def set_constructor(self, constructor: ConstructorAutomovil):
        self._constructor = constructor

    def construir_modelo_basico(self) -> None:
        self._constructor.set_motor("V4 1.6L") \
                         .set_color("Blanco") \
                         .set_llantas("Acero 15 pulgadas")

    def construir_modelo_lujo(self) -> None:
        self._constructor.set_motor("V8 5.0L") \
                         .set_color("Negro Mate") \
                         .set_llantas("Aleación 20 pulgadas") \
                         .set_sistema_sonido("Bose Surround") \
                         .set_interiores("Cuero Premium") \
                         .set_techo_solar(True) \
                         .set_gps(True)