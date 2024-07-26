print("Bienvenida a la Calculadora de IMC")
print()
nombre= input("Introduce tu nombre: ")
print ("Hola",nombre,"estamos felices de poder ayudarte!")

print()

estatura_cm=input("Introduzca su estatura en cm: ")

while not estatura_cm.isdigit():
    print("Por favor, introduzca una estatura válida.")
    estatura_cm = input("Introduzca su estatura en cm: ")

estatura_m = int(estatura_cm) / 100

peso=input("Introduzca su peso en kg: ")

while not peso.isdigit():
    print("Por favor, introduzca un peso válido")
    peso = input("Introduzca su peso en kg: ")

peso= float(peso)
    
denominador= estatura_m**2
numerador= peso
IMC= numerador/denominador
print()
IMC_redondeado = round(IMC, 2)
print("Su IMC es igual a: ",IMC_redondeado)

if IMC <= 18.5:
    print("Clasificación: Bajo Peso")
    print("Consuma suficientes calorías.")
elif 18.5 <=IMC <= 24.9:
    print("Clasificación: Normal")
    print("Felicidades, tiene un peso adecuado!!")
elif 25 <= IMC <= 29.9:
    print("Clasificación: Sobrepeso")
    print("Cuide su alimentación y realice ejercicio regular.")
elif 30 <= IMC <= 34.9:
    print("Clasificación: Obesidad 1")
    print("Realice dieta y ejercicio regular.")
elif 35 <= IMC <=39.9:
    print("Clasificación: Obesidad 2")
    print("Precaución! Realice dieta con disciplina y ejercicio regular.")
elif IMC >= 40:
    print("Clasificación: Obesidad 3")
    print("Peligro! Realice dieta con disciplina y consulte a un nutriólogo.")
print()
print("Gracias", nombre, "por usar nuestra calculadora!")





 
