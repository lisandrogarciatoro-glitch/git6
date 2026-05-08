class gato():
    def __init__(self, nombre, colordepelo, colordeojos, hambre, cansancio, sucio, felicidad):
        self.nombre = nombre
        self.colordepelo = colordepelo
        self.colordeojos = colordeojos
        self.hambre = hambre
        self.cansancio = cansancio        
        self.sucio = sucio
        self.felicidad = felicidad
    def jugar(self):
        if self.cansancio:
            print("el gato te araña")
        elif self.hambre:
            print("el gato te saca un dedo")
        else:
            print("el gato se divierte")
            self.hambre = True
            self.cansancio = True
    def dormir(self):
        if self.cansancio:
            print("el gato duerme")
        else:
            print("el gato no quiere dormir")
    def acariciar(self):
        if self.cansancio:
            print("el gato te odia")
        elif self.hambre:
            print("el gato te muerde")
        else:
            print("brrr")
    def comer(self):
        if  self.hambre:
            print("el gato come ñam ñam")
            self.hambre = False
    def bañarse(self):
        if self.sucio:
            print("el gato se baña")
        else:
            print("el gato esta limpio")
    def morder(self):
        if self.felicidad:
            print("el gato no te muerde porque esta feliz")
        else:
            print("el gato te muerde fuerte y te arranca un pedazo de piel")
gatito = gato("candelaria", "marrones claros con negros", "verde claro", True, False, True, False)
gatito.morder()