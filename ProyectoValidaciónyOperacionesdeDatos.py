VERDE = "\033[92m"
CIAN = "\033[96m"
AMARILLO = "\033[93m"
RESET = "\033[0m"

print(f"{VERDE}Bienvenido a la Calculadora de Longitud de Palabras{RESET}") #Muestra un mensaje de bienvenida en color.
print()
while True: #Inicia un bucle infinito para solicitar palabras hasta que se ingrese una palabra válida.
 palabra=input("Ingrese una palabra: ") #Se le pide al usuario que ingrese una palabra.
 x = len(palabra) #Con esta función se mide la longitud de la palabra.

 if (x >= 4 and x <= 8): #Si la palabra tiene mas o igual a cuatro letras y menos o igual a ocho letras, la palabra es correcta.
    print(f"Esta palabra tiene {x} letras, esta palabra es correcta, buen trabajo!") #Se imprime un mensaje de validación de la palabra.
    break #Si se cumple la condición, se rompe el ciclo.
 
 elif (x < 4): #Cuando la longitud de la palabra es menor a 4 letras, se realizan las siguientes operaciones.
    faltan = 4 - x #Se hace una resta para calcular cuántas letras faltan para completar un total de cuatro.
    if faltan == 1: #Si solo falta una letra, se despliega un mensaje en singular.
        print(f"Esta palabra tiene {x} letras, hace falta {faltan} letra.") #Muestra un mensaje indicando que falta una letra para completar el mínimo de cuatro.
    else: #Sino, cuando falta más de una letra, se despliega un mensaje en plural.
        print(f"Esta palabra tiene {x} letras, hacen falta {faltan} letras.") #Muestra un mensaje indicando cuántas letras faltan para alcanzar el mínimo de cuatro cuando faltan más de una.
   
 elif (x > 8): #Cuando la longitud de la palabra es mayor a 8 letras, se realizan las siguientes operaciones.
    sobran = x - 8 #Se hace una resta para calcular cuántas letras sobran para completar un total de ocho.
    if sobran == 1: #Si solo sobra una letra, se despliega un mensaje en singular.
        print(f"Esta palabra tiene {x} letras, sobra {sobran} letra.")
    else: #Sino, cuando sobra más de una letra, se despliega un mensaje en plural.
        print(f"Esta palabra tiene {x} letras, sobran {sobran} letras.")
print()
print(f"{AMARILLO}¡Gracias por usar esta Calculadora de Longitud de Palabras!{RESET}") #Mensaje de despedida.
print()

#Este es el segundo programa

print(f"{VERDE}Bienvenido a la Identificadora de Cuadrante{RESET}") #Se muestra un mensaje de bienvenida.
print("Instrucción: Según las coordenadas que proporcione, se\ndeterminará el cuadrante correspondiente en el Plano Cartesiano.") #Se muestra un mensaje para explicar el programa.
print()

while True: #Bucle infinito para pedir el valor de X.
 
 Valor_X= int(input("Ingrese el valor en X: ")) #Solicitar al usuario el valor de X.

 if Valor_X==0: #Si el valor de X es 0, se despliega un mensaje que menciona que se encuentra en el origen.
    print(f"El valor {Valor_X} se encuentra en el origen, por favor, ingresa un valor diferente.")
    continue #Volver a pedir el valor de X si es 0. Se reinicia el bucle.
 break #Si el valor es diferente de 0, sale del bucle.

while True: #Bucle infinito para pedir el valor de Y.
 Valor_Y = int(input("Ingrese un valor en Y: ")) #Solicitar al usuario el valor de Y.

 if Valor_Y==0: #Si el valor de Y es 0, se despliega un mensaje que menciona que se encuentra en el origen.
   print(f"El valor {Valor_Y} se encuentra en el origen, por favor, ingresa un valor diferente.")
   continue #Volver a pedir el valor de Y si es 0. Se reinicia el bucle.
 break #Si el valor es diferente de 0, sale del bucle.

print()
print(f"Sus coordenadas son {Valor_X},{Valor_Y}") #Imprimir las coordenadas ingresadas.
print()    

#Identificar y mostrar en qué cuadrante se encuentra el punto según las coordenadas.
if Valor_X >0 and Valor_Y >0:
  print(f"{CIAN}Este punto en el plano está en el Primer Cuadrante{RESET}")
  print()
  print("       │   ") 
  print("       │   ")     
  print("       │   ")     
  print("       │   ")    
  print("       │        I")      
  print("       │   ")      
  print("       │   ")     
  print("       │   ")
  print("       │   ")
  print("───────┼──────────────────")
  print("       │   ")   
  print()     

if Valor_X >0 and Valor_Y < 0:
  print(f"{CIAN}Este punto en el plano está en el Cuarto Cuadrante{RESET}")
  print()
  print("       │   ")
  print("───────┼──────────────────")            
  print("       │   ") 
  print("       │   ")     
  print("       │   ")     
  print("       │   ")    
  print("       │        IV")      
  print("       │   ")
  print("       │   ")     
  print("       │   ")
  print("       │   ")   
  print()
 
if Valor_X <0 and Valor_Y>0:
  print(f"{CIAN}Este punto en el plano está en el Segundo Cuadrante{RESET}")
  print()
  print("                  │   ") 
  print("                  │   ")     
  print("                  │   ")     
  print("                  │   ")    
  print("        II        │   ")      
  print("                  │   ")
  print("                  │   ")     
  print("                  │   ")
  print("                  │   ")
  print("──────────────────┼───────")
  print("                  │   ")  
  print()   

if Valor_X <0 and Valor_Y <0:
  print(f"{CIAN}Este punto en el plano está en el Tercer Cuadrante{RESET}")
  print()
  print("                  │   ")
  print("──────────────────┼───────")            
  print("                  │   ") 
  print("                  │   ")     
  print("                  │   ")     
  print("                  │   ")    
  print("       III        │   ")      
  print("                  │   ")
  print("                  │   ")     
  print("                  │   ")
  print("                  │   ")   
  print()

print(f"{AMARILLO}¡Gracias por usar esta Identificadora de Cuadrante!{RESET}") #Mensaje de despedida.
print()