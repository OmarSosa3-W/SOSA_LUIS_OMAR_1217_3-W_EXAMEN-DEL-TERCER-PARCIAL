print() #para dejar una line en blannco
print("SOSA LUIS OMAR 1217_3-W: MI PRACTICA DE CLASS") #el nombre del creador
print() #para dejar una line en blannco

# definir la clase y las funciones para que muestre los datos 
class Persona:
    def __init__(self, nombre, edad): 
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")
        print() #para dejar una line en blannco
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            print(f"{self.nombre} es mayor de edad y le gusta el metal.")
            print() #para dejar una line en blannco
        else:
            print(f"{self.nombre} no es mayor de edad y le gusta el metal.")
            print() #para dejar una line en blannco
#los nombre y la cantidad de personas que mostrara
persona = Persona("Omar", 20)
persona.mostrar_datos()
persona.es_mayor_de_edad()
