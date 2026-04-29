import os

# --- ESTRUCTURA INICIAL ---
datos_escuela = {
    "Alumnos": []
}

# --- FUNCIONES DE GESTIÓN ---

def agregar_alumno(sistema):
    print("\n--- Registrar Nuevo Alumno ---")
    nuevo_alumno = {
        "Nombre": input("Nombre: "),
        "Apellido": input("Apellido: "),
        "DNI": input("DNI: "),
        "Fecha de nacimiento": input("Fecha de nacimiento (DD/MM/AAAA): "),
        "Tutor": input("Nombre del Tutor: "),
        "Notas": [],
        "Faltas": 0,
        "Amonestaciones": 0
    }
    sistema["Alumnos"].append(nuevo_alumno)
    print("¡Alumno registrado con éxito!")

def mostrar_alumnos(sistema):
    if not sistema["Alumnos"]:
        print("\nNo hay alumnos registrados.")
        return

    print("\n--- Lista de Alumnos ---")
    for i, alumno in enumerate(sistema["Alumnos"]):
        print(f"{i + 1}. {alumno['Apellido']}, {alumno['Nombre']} (DNI: {alumno['DNI']})")
        print(f"   Tutor: {alumno['Tutor']} | Faltas: {alumno['Faltas']} | Amonestaciones: {alumno['Amonestaciones']}")
        print(f"   Notas: {alumno['Notas']}")
        print("-" * 30)

def modificar_alumno(sistema):
    mostrar_alumnos(sistema)
    if not sistema["Alumnos"]: return
    
    indice = int(input("Seleccione el número del alumno a modificar: ")) - 1
    if 0 <= indice < len(sistema["Alumnos"]):
        alumno = sistema["Alumnos"][indice]
        print("\n¿Qué desea modificar?")
        print("1. Faltas (+1)\n2. Amonestaciones (+1)\n3. Agregar Nota\n4. Cambiar Tutor")
        
        opcion = input("Opción: ")
        if opcion == "1":
            alumno["Faltas"] += 1
        elif opcion == "2":
            alumno["Amonestaciones"] += 1
        elif opcion == "3":
            nota = float(input("Ingrese la nota: "))
            alumno["Notas"].append(nota)
        elif opcion == "4":
            alumno["Tutor"] = input("Nuevo nombre de tutor: ")
        
        print("Datos actualizados.")
    else:
        print("Índice inválido.")

def expulsar_alumno(sistema):
    mostrar_alumnos(sistema)
    if not sistema["Alumnos"]: return
    
    indice = int(input("Seleccione el número del alumno a expulsar (borrar): ")) - 1
    if 0 <= indice < len(sistema["Alumnos"]):
        eliminado = sistema["Alumnos"].pop(indice)
        print(f"El alumno {eliminado['Nombre']} {eliminado['Apellido']} ha sido removido del sistema.")
    else:
        print("Índice inválido.")

# --- MENÚ PRINCIPAL ---

def menu():
    while True:
        print("\n--- SISTEMA DE GESTIÓN ESCOLAR ---")
        print("1. Mostrar alumnos")
        print("2. Agregar alumno")
        print("3. Modificar datos de alumno")
        print("4. Expulsar alumno")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            mostrar_alumnos(datos_escuela)
        elif opcion == "2":
            agregar_alumno(datos_escuela)
        elif opcion == "3":
            modificar_alumno(datos_escuela)
        elif opcion == "4":
            expulsar_alumno(datos_escuela)
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()