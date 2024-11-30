print() #para dejar una linea en blanco al ejecutar
print("Sosa Luis Omar: 1217_3-w mi practica de class") #El nombre del creador 
print() #para dejar una linea en blanco al ejecutar

class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}, Nota: {self.nota}")
        print() #para dejar una linea en blanco al ejecutar
    def mostrar_resultado(self):
        print("Aprobado" if self.nota >= 6 else "No aprobado")
        print() #para dejar una linea en blanco al ejecutar
alumno = Alumno("Juan", 8)
alumno.mostrar_datos()
alumno.mostrar_resultado()