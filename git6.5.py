import pickle
import os

class Alumno:
    def __init__(self, nombre, apellido, fecha_nac, dni, tutor):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nac = fecha_nac
        self.dni = dni
        self.tutor = tutor
        self.notas = []
        self.faltas = 0
        self.amonestaciones = 0

    def __str__(self):
        return (f"DNI: {self.dni} | {self.apellido}, {self.nombre} | "
                f"Tutor: {self.tutor} | Faltas: {self.faltas} | "
                f"Amonestaciones: {self.amonestaciones} | Notas: {self.notas}")

class Escuela:
    def __init__(self, archivo_datos='alumnos.dat'):
        self.archivo_datos = archivo_datos
        self.alumnos = self.cargar_datos()

    def agregar_alumno(self):
        print("\n--- Registro de Nuevo Alumno ---")
        dni = input("DNI: ")
        if dni in self.alumnos:
            print("Error: Ya existe un alumno con ese DNI.")
            return
        
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        fecha_nac = input("Fecha de Nacimiento (DD/MM/AAAA): ")
        tutor = input("Nombre del Tutor: ")
        
        nuevo_alumno = Alumno(nombre, apellido, fecha_nac, dni, tutor)
        self.alumnos[dni] = nuevo_alumno
        self.guardar_datos()
        print("Alumno registrado con éxito.")

    def mostrar_alumnos(self):
        if not self.alumnos:
            print("\nNo hay alumnos registrados.")
        for alumno in self.alumnos.values():
            print(alumno)

    def modificar_alumno(self):
        dni = input("\nIngrese el DNI del alumno a modificar: ")
        if dni in self.alumnos:
            al = self.alumnos[dni]
            print("Deje en blanco para no modificar.")
            al.nombre = input(f"Nombre ({al.nombre}): ") or al.nombre
            al.apellido = input(f"Apellido ({al.apellido}): ") or al.apellido
            al.tutor = input(f"Tutor ({al.tutor}): ") or al.tutor
            
            try:
                faltas = input(f"Faltas ({al.faltas}): ")
                if faltas: al.faltas = int(faltas)
                
                amon = input(f"Amonestaciones ({al.amonestaciones}): ")
                if amon: al.amonestaciones = int(amon)
                
                nota = input("Agregar una nueva nota (Enter para saltar): ")
                if nota: al.notas.append(float(nota))
            except ValueError:
                print("Error: Ingrese valores numéricos válidos.")
            
            self.guardar_datos()
            print("Datos actualizados.")
        else:
            print("Alumno no encontrado.")

    def expulsar_alumno(self):
        dni = input("\nIngrese el DNI del alumno a expulsar: ")
        if dni in self.alumnos:
            del self.alumnos[dni]
            self.guardar_datos()
            print("Alumno eliminado del sistema.")
        else:
            print("Alumno no encontrado.")

    def guardar_datos(self):
        with open(self.archivo_datos, 'wb') as f:
            pickle.dump(self.alumnos, f)

    def cargar_datos(self):
        if os.path.exists(self.archivo_datos):
            with open(self.archivo_datos, 'rb') as f:
                return pickle.load(f)
        return {}

def menu():
    escuela = Escuela()
    while True:
        print("\n--- SISTEMA DE GESTIÓN ESCOLAR ---")
        print("1. Agregar Alumno")
        print("2. Mostrar Alumnos")
        print("3. Modificar Alumno (Notas, Faltas, Datos)")
        print("4. Expulsar Alumno")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1': escuela.agregar_alumno()
        elif opcion == '2': escuela.mostrar_alumnos()
        elif opcion == '3': escuela.modificar_alumno()
        elif opcion == '4': escuela.expulsar_alumno()
        elif opcion == '5': break
        else: print("Opción no válida.")

if __name__ == "__main__":
    menu()