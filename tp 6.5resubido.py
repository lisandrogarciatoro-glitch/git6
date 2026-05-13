import os

# Nombre del archivo de texto
ARCHIVO = "datos_alumnos.txt"

# --- FUNCIONES DE PERSISTENCIA ---

def guardar_datos(sistema):
    """Guarda la lista de alumnos en el archivo de texto."""
    with open(ARCHIVO, "w") as f:
        for alumno in sistema["Alumnos"]:
            # Convertimos la lista de notas a una cadena separada por comas
            notas_str = ",".join(map(str, alumno["Notas"]))
            # Creamos una línea con todos los datos separados por ';'
            linea = f"{alumno['Nombre']};{alumno['Apellido']};{alumno['DNI']};{alumno['Fecha de nacimiento']};{alumno['Tutor']};{alumno['Faltas']};{alumno['Amonestaciones']};{notas_str}\n"
            f.write(linea)

def cargar_datos():
    """Lee el archivo de texto y reconstruye la estructura de datos."""
    sistema = {"Alumnos": []}
    if not os.path.exists(ARCHIVO):
        return sistema

    with open(ARCHIVO, "r") as f:
        for linea in f:
            datos = linea.strip().split(";")
            if len(datos) < 8: continue  # Salta líneas mal formadas
            
            alumno = {
                "Nombre": datos[0],
                "Apellido": datos[1],
                "DNI": datos[2],
                "Fecha de nacimiento": datos[3],
                "Tutor": datos[4],
                "Faltas": int(datos[5]),
                "Amonestaciones": int(datos[6]),
                # Convertimos la cadena de notas de nuevo a una lista de floats
                "Notas": [float(n) for n in datos[7].split(",")] if datos[7] else []
            }
            sistema["Alumnos"].append(alumno)
    return sistema

# --- ESTRUCTURA INICIAL ---
datos_escuela = cargar_datos()

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
    guardar_datos(sistema) # Guardar al agregar
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
    
    try:
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
            
            guardar_datos(sistema) # Guardar al modificar
            print("Datos actualizados.")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada no válida.")

def expulsar_alumno(sistema):
    mostrar_alumnos(sistema)
    if not sistema["Alumnos"]: return
    
    try:
        indice = int(input("Seleccione el número del alumno a expulsar: ")) - 1
        if 0 <= indice < len(sistema["Alumnos"]):
            eliminado = sistema["Alumnos"].pop(indice)
            guardar_datos(sistema) # Guardar al eliminar
            print(f"El alumno {eliminado['Nombre']} ha sido removido.")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada no válida.")

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
            print("Saliendo y guardando...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()