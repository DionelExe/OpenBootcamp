class Alumno:
    def __init__(self, nombre, apellido, nota):
        self.nonbre = nombre
        self.apellido = apellido
        self.nota = nota

    def nombreCompleto(self):
        print(f"El nombre del alumno es: {self.nonbre} y el apellido es: {self.apellido}")

    def calificacion(self):
        if self.nota >= 7:
            print("El alumno aprobo")
        else:
            print("El alumno desaprobo")

tato = Alumno("Gaston","Paredes",6)
tato.nombreCompleto()
tato.calificacion()

