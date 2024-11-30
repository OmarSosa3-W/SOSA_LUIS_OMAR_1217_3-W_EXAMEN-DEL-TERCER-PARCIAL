# SOSA_LUIS_OMAR_1217_3-W_EXAMEN-DEL-TERCER-PARCIAL
Examen del tercer parcial
# PROGRAMA 1:
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

![image](https://github.com/user-attachments/assets/4a64b955-2028-4986-8743-6e64d7a22124)
![image](https://github.com/user-attachments/assets/d3ccc631-f3ac-4aee-a827-d1c320fee14b)

# PROGRAMA 2:
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

![image](https://github.com/user-attachments/assets/14838ef3-8fa5-498e-9b72-8f3bd948f620)
![image](https://github.com/user-attachments/assets/1f523c8d-2cec-4876-9ef5-94e4ef63b7ee)

# PROGRAMA 3:
print() #para dejar una line en blannco
print("SOSA LUIS OMAR 1217_3-W MI PRACTICA DE TRAINGULOS") #el nombre del creador
print() #para dejar una line en blannco
def lado_mayor(lado1, lado2, lado3):
    print("El lado mayor es:", max(lado1, lado2, lado3))
def tipo_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        print("El triángulo es equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("El triángulo es isósceles.")
    else:
        print("El triángulo es escaleno.")
print() #para dejar una line en blannco
lado1 = float(input("ingrese el primer lado del triángulo: ")) #pide ingresar el primer valor 
print() #para dejar una line en blannco
lado2 = float(input("ingrese el segundo lado del triángulo: ")) #pide ingresar el segundo valor 
print() #para dejar una line en blannco
lado3 = float(input("ingrese el tercer lado del triangulo: ")) #pide ingresar el tercer valor 
print() #para dejar una line en blannco
lado_mayor(lado1, lado2, lado3)
print() #para dejar una line en blannco
tipo_triangulo(lado1, lado2, lado3)
print() #para dejar una line en blannco

![image](https://github.com/user-attachments/assets/3658bb19-68a8-4d76-86b3-65c58d9fe9eb)
![image](https://github.com/user-attachments/assets/75b5eae6-f5f7-42df-a80b-1625c3d63a11)

# PROGRAMA 4:
print() #para dejar una line en blannco
print("SOSA LUIS OMAR 1217_3-W MI PRACTICA DE CALCULADORA")
print() #para dejar una line en blannco
class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def sumar(self):
        return self.a + self.b
    def restar(self):
        return self.a - self.b
    def multiplicar(self):
        return self.a * self.b
    def dividir(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Error: División por cero"
        print()
a = int(input("Ingrese el primer número, el valor de (a): "))
print()
b = int(input("Ingrese el segundo número, el valor de (b): "))
print()
calc = Calculadora(a, b)
print("La suma es:", calc.sumar())
print() #para dejar una line en blannco
print("La resta es:", calc.restar())
print() #para dejar una line en blannco
print("La multiplicación es:", calc.multiplicar())
print() #para dejar una line en blannco
print("La división es:", calc.dividir())
print() #para dejar una line en blannco

![image](https://github.com/user-attachments/assets/b01daeac-8365-4832-b48c-867b1b75011a)
![image](https://github.com/user-attachments/assets/571a85f2-7953-406c-a20e-8883ffd4dd5a)

# PROGRAMA 5:
print() #para dejar una line en blannco
print("SOSA LUIS OMAR 1217_3-W: MI PRACTICA DE AGENDAS") #el nombre del creador
print() #para dejar una line en blannco
class Agenda: #se crea la agenda o la clase 
    def __init__(self): #se declara la función y sus variables 
        self.contactos = []
    def añadir_contacto(self):
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        email = input("Email: ")
        self.contactos.append({"nombre": nombre, "telefono": telefono, "email": email})
        # aqui se inicia otra función
    def listar_contactos(self): #la función para los datos del usuario
        for c in self.contactos:
            print(f"Nombre: {c['nombre']}, Teléfono: {c['telefono']}, Email: {c['email']}")
    def buscar_contacto(self): #la función para buscar al contacto
        nombre = input("Buscar nombre: ")
        for c in self.contactos:
            if c["nombre"] == nombre:
                print(f"Nombre: {c['nombre']}, Teléfono: {c['telefono']}, Email: {c['email']}")
                return
        print("No encontrado.")
    def editar_contacto(self): #la función para editar el nombre 
        nombre = input("Editar nombre: ")
        for c in self.contactos:
            if c["nombre"] == nombre:
                c["telefono"] = input("Nuevo teléfono: ")
                c["email"] = input("Nuevo email: ")
                return
        print("No encontrado.")
    def cerrar_agenda(self):
        print("Agenda cerrada.")
        exit ()
agenda = Agenda()
while True:   #usamos while para dar la instrucción de un switch y nos deje elegir la opcion que queremos hacer con la agenda 
    print("\n1. Añadir")
    print("2. Listar")
    print("3. Buscar")
    print("4. Editar")
    print("5. Cerrar")
    opcion = input("Elija opción: ")
    if opcion == "1":
        agenda.añadir_contacto()      
        """
        esto nos da la opción de poder elegir que queremos hacer con nuesta agenda, se debe elegir una de la opciones en pantalla, se lo contrario: error
        """
    elif opcion == "2":
        agenda.listar_contactos()
    elif opcion == "3":
        agenda.buscar_contacto()
    elif opcion == "4":
        agenda.editar_contacto()
    elif opcion == "5":
        agenda.cerrar_agenda()
    else:
        print("Opción no válida.") #esto lo muestra en caso de poner un opción que no esta en la lista, osea un numero mayor que el 5

![image](https://github.com/user-attachments/assets/9257e5a0-2439-4b06-b7d2-211b1f0aad23)
![image](https://github.com/user-attachments/assets/3318d1f9-fe8a-4204-bc85-ca4f1c698446)
![image](https://github.com/user-attachments/assets/170b06a4-88ee-4db4-9239-eb9b37f3bfe4)
