RESET = '\033[0m'
BOLD = '\033[1m' 
BLUE = '\033[94m'
CYAN = '\033[36m'
UNDERLINE = '\033[4m' 
YELLOW = '\033[33m'
GREEN_LIGHT = '\033[92m'
GREEN = '\033[32m'
RED_LIGHT = '\033[91m'
RED = '\033[31m'

print(f"{BOLD}{BLUE}Bienvenida a la Calculadora de IMC{RESET}")
print()
nombre= input("Introduce tu nombre: ")
apellidopaterno= input("Introduce tu apellido paterno: ")
apellidomaterno= input("Introduce tu apellido materno: ")
print()
print (f"{CYAN}Hola",nombre,apellidopaterno,apellidomaterno,f"{CYAN}estamos felices de poder ayudarte!{RESET}")
 
print()
edad= input("Introduzca su edad: ")
while not edad.isdigit():
    print("Por favor, introduzca una edad válida.")
    edad= input("Introduzca su edad: ")

edad=int(edad)

if (edad < 18):
 print("Usted es menor de edad")
 print(f"{RED_LIGHT}Use la calculadora sabiamente{RESET}")
 print()
else:
 print("Usted es mayor de edad")

estatura_cm=input("Introduzca su estatura en cm: ")

while not estatura_cm.isdigit():
    print("Por favor, introduzca una estatura válida.")
    estatura_cm = input("Introduzca su estatura en cm: ")

estatura_m = int(estatura_cm) / 100

peso=input("Introduzca su peso en kg: ")

while not peso.isdigit():
    print("Por favor, introduzca un peso válido.")
    peso = input("Introduzca su peso en kg: ")

peso= float(peso)
    
denominador= estatura_m**2
numerador= peso
IMC= numerador/denominador
print()
IMC_redondeado = round(IMC, 2)
print(f"{UNDERLINE}Su IMC es igual a:{RESET}",IMC_redondeado)

if IMC <= 18.5:
    print("Clasificación: Bajo Peso")
    print(f"{GREEN_LIGHT}Consuma suficientes calorías.{RESET}")
elif 18.5 <=IMC <= 24.9:
    print("Clasificación: Normal")
    print(f"{GREEN}Felicidades, tiene un peso adecuado!!{RESET}")
elif 25 <= IMC <= 29.9:
    print("Clasificación: Sobrepeso")
    print(f"{GREEN}Cuide su alimentación y realice ejercicio regular.{RESET}")
elif 30 <= IMC <= 34.9:
    print("Clasificación: Obesidad 1")
    print(f"{RED_LIGHT}Realice dieta y ejercicio regular.{RESET}")
elif 35 <= IMC <=39.9:
    print("Clasificación: Obesidad 2")
    print(f"{RED_LIGHT}Precaución! Realice dieta con disciplina y ejercicio regular.{RESET}")
elif IMC >= 40:
    print("Clasificación: Obesidad 3")
    print(f"{RED}Peligro! Realice dieta con disciplina y consulte a un nutriólogo.{RESET}")
print()
print(f"{YELLOW}¡Gracias", nombre, f"{YELLOW}por usar nuestra calculadora!{RESET}")






 


