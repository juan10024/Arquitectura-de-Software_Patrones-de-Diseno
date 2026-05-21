from builder import ConstructorAutomovilConcreto
from director import DirectorAutomovil

def main():
    constructor = ConstructorAutomovilConcreto()
    director = DirectorAutomovil(constructor)

    print("--- Construyendo Versión Básica ---")
    director.construir_version_basica()
    auto_basico = constructor.construir()
    print(auto_basico)

    print("\n--- Construyendo Versión Full ---")
    director.construir_version_full()
    auto_lujo = constructor.construir()
    print(auto_lujo)

    print("\n--- Construyendo Versión Personalizada - Sin Director ---")
    # El cliente también puede usar el builder directamente para personalizaciones únicas
    auto_custom = (constructor.set_motor("V6 3.0L")
                              .set_color("Rojo Cereza")
                              .set_llantas("Deportivas 18 pulgadas")
                              .set_gps(True)
                              .construir())
    print(auto_custom)

if __name__ == "__main__":
    main()