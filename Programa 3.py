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