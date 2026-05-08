#1. Clase Rectángulo
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura
#2. Clase Mate
class Mate:
    def __init__(self, n):
        self.n = n  # Cantidad máxima
        self.cebadas_restantes = n
        self.esta_lleno = False

    def cebar(self):
        if self.esta_lleno:
            raise Exception("¡Cuidado! ¡Te quemaste!")
        self.esta_lleno = True

    def beber(self):
        if not self.esta_lleno:
            raise Exception("¡El mate está vacío!")
        
        if self.cebadas_restantes > 0:
            self.cebadas_restantes -= 1
        else:
            print("Advertencia: el mate está lavado.")
        
        self.esta_lleno = False
#3. Botella y Sacacorchos
class Corcho:
    def __init__(self, bodega):
        self.bodega = bodega

class Botella:
    def __init__(self, corcho=None):
        self.corcho = corcho

class Sacacorchos:
    def __init__(self):
        self.corcho_en_uso = None

    def destapar(self, botella):
        if botella.corcho is None:
            raise Exception("La botella ya está destapada.")
        if self.corcho_en_uso is not None:
            raise Exception("El sacacorchos ya tiene un corcho.")
        
        self.corcho_en_uso = botella.corcho
        botella.corcho = None

    def limpiar(self):
        if self.corcho_en_uso is None:
            raise Exception("No hay un corcho que sacar.")
        self.corcho_en_uso = None
#4. Heladería (Herencia)
class Restaurante:
    def __init__(self, restaurante_nombre, tipo_comida):
        self.restaurante_nombre = restaurante_nombre
        self.tipo_comida = tipo_comida

    def describir_restaurante(self):
        print(f"Restaurante: {self.restaurante_nombre}, Especialidad: {self.tipo_comida}")

    def abrir_restaurante(self):
        print(f"El restaurante {self.restaurante_nombre} ahora está abierto.")

class Heladeria(Restaurante):
    def __init__(self, restaurante_nombre, tipo_comida, sabores):
        super().__init__(restaurante_nombre, tipo_comida)
        self.sabores = sabores

    def mostrar_sabores(self):
        print(f"Sabores disponibles: {', '.join(self.sabores)}")

# Instancia y prueba
mi_heladeria = Heladeria("Frozen", "Helados", ["Chocolate", "Vainilla", "Menta"])
mi_heladeria.mostrar_sabores()
#5. Personajes, Soldados y Campesinos
class Personaje:
    def __init__(self, vida, posicion, velocidad):
        self.vida = vida
        self.posicion = posicion  # Ejemplo: [x, y]
        self.velocidad = velocidad

    def recibir_attack(self, cantidad):
        self.vida -= cantidad
        if self.vida <= 0:
            raise Exception("El personaje ha muerto.")

    def mover(self, direccion):
        # Simplificando la dirección (ej: "norte", "sur", etc.)
        print(f"Moviéndose hacia {direccion} a {self.velocidad} km/h.")

class Soldado(Personaje):
    def __init__(self, vida, posicion, velocidad, ataque):
        super().__init__(vida, posicion, velocidad)
        self.ataque = ataque

    def atacar(self, otro_personaje):
        otro_personaje.recibir_attack(self.ataque)

class Campesino(Personaje):
    def __init__(self, vida, posicion, velocidad, cosecha):
        super().__init__(vida, posicion, velocidad)
        self.cosecha = cosecha

    def cosechar(self):
        return self.cosecha
#6 y 7. Usuarios y Admin
class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

    def describir_usuario(self):
        print(f"Perfil: {self.nombre} {self.apellido} ({self.email})")

    def saludar_usuario(self):
        print(f"Hola, {self.nombre}, ¡un gusto verte de nuevo!")

class Admin(Usuario):
    def __init__(self, nombre, apellido, email, privilegios):
        super().__init__(nombre, apellido, email)
        self.privilegios = privilegios

    def mostrar_privilegios(self):
        print(f"Privilegios del admin: {', '.join(self.privilegios)}")
#8. Clase Privilegios como Atributo
class Privilegios:
    def __init__(self, privilegios):
        self.privilegios = privilegios

    def mostrar_privilegios(self):
        print(f"Privilegios: {', '.join(self.privilegios)}")

class Admin(Usuario):
    def __init__(self, nombre, apellido, email, lista_privilegios):
        super().__init__(nombre, apellido, email)
        # Se crea la instancia de la clase Privilegios como atributo
        self.privilegios = Privilegios(lista_privilegios)

# Prueba
admin_pro = Admin("Juan", "Perez", "juan@web.com", ["banear", "borrar"])
admin_pro.privilegios.mostrar_privilegios()
