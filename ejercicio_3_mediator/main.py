from mediador import SalaChatMediador
from usuario import UsuarioConcreto

def main():
    # Crear El Mediador
    sala_arquitectura = SalaChatMediador()

    # Crear los componentes. Solo se inyecta la dependencia del Mediador.
    dev1 = UsuarioConcreto(sala_arquitectura, "Alice")
    dev2 = UsuarioConcreto(sala_arquitectura, "Bob")
    dev3 = UsuarioConcreto(sala_arquitectura, "Charlie")

    print("\n--- Inicio de la Conversación ---")
    
    dev1.enviar("Hola equipo, ¿cómo vamos con los diagramas ER de la Etapa 2?")
    dev3.enviar("Todo en orden, acabo de validar las cardinalidades.")
    
    print("\n--- Modificación Dinámica de la Red ---")
    # Agregar un usuario nuevo.
    qa1 = UsuarioConcreto(sala_arquitectura, "Diana de QC")
    qa1.enviar("Acabo de unirme, por favor compartan los esquemas lógicos.")

if __name__ == "__main__":
    main()