class Vehiculo:
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas        
    
    def colour(self):
        print("Es de color:",self.color)

    def wheels(self):
        print(f"Tiene {self.ruedas} ruedas")

    def doors(self):
        print(f"Tiene {self.puertas} puertas")            

class Auto(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        

    def speed(self):
        print(f"Velocidad Maxima: {self.velocidad} km/h")

    def cilindrate(self):
        print(f"Tiene {self.cilindrada} cilindros")

    def all(self):
        self.colour()
        self.wheels()
        self.doors()
        self.speed()
        self.cilindrate() 


camaro = Auto("rojo", 4, 5, 160, 4)
camaro.all()