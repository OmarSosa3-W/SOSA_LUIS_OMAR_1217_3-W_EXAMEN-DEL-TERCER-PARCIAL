print() #para dejar una line en blannco
print("SOSA LUIS OMAR 1217_3-W MI PRACTICA DE CALCULADORA") #el nombre del creador del programa 
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