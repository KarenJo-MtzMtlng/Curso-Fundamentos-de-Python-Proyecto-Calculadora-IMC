print("Bienvenido a la Calculadora de Longitud de Palabras")

while True: 
 palabra=input("Ingrese una palabra: ")
 x = len(palabra)

 if (x >= 4 and x <= 8):
    print(f"Esta palabra tiene {x} letras, esta palabra es correcta, buen trabajo!")
    break

 elif (x < 4):
    faltan = 4 - x
    if faltan == 1 :
        print(f"Esta palabra tiene {x} letras, hace falta {faltan} letra.")
    else:
        print(f"Esta palabra tiene {x} letras, hacen falta {faltan} letras.")
   

 elif (x > 8):
    sobran = x - 8
    if sobran == 1:
        print(f"Esta palabra tiene {x} letras, sobra {sobran} letra.")
    else:
        print(f"Esta palabra tiene {x} letras, sobran {sobran} letras.")


#Este es el segundo programa

print("Bienvenido a la Identificadora de Cuadrante")

print("Instrucción: Con base a las coordenadas que ingrese ,/n se le dará su respectivo cuadrante en el Sistema Cartesiano")