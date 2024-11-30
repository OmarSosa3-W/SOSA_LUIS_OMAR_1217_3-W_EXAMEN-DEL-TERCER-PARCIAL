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