import random
import numpy as np

menu = int(input("ingrse su opccion \n 1)calcular potencia de circuito \n 2)calculo de x numeros aleatorios con rango \n 3) un programa para el cálculo de volúmenes \n 4) programa que le permita al usuario escoger entre robot \n 5) programa que realice la pregunta ¿Desea continuar Si/No?"))
if menu == 1:
    """
    1)Realice un programa que calcule la potencia que consume un circuito ingresando por teclado el
    valor de corriente y voltaje.
    """
    voltaje = int(input("ingrese el voltaje que tiene el circuto: "))
    corriente = int(input("ingrese la corriente que atraviesa el circuito: "))

    def calculoPotencia(voltaje, corriente):
        
        return voltaje * corriente

    potencia = calculoPotencia(voltaje, corriente)
    print(f"el resultado es {potencia}")

elif menu == 2:
    """2. Realice un programa que calcule X números
    aleatorios en un rango determinado por el usuario."""
    caantidadNumerosAle= int(input("ingrese la cantidad de numeros aleatorios que quiere calcular: "))
    numeroMin = int(input("ingrese el valor desde que desea calcular: "))
    numeroMax = int(input("ingrese el valor hasta el que desea calcular: "))
    numeroAleatorio = np.random.randint(numeroMin, numeroMax, caantidadNumerosAle)

    print("sus numero/s aleatroios: ", numeroAleatorio)
elif menu == 3:
    """
    3)Realice un programa para el cálculo de volúmenes (Prisma, Pirámide, Cono truncado, Cilindro)
    donde el usuario pueda seleccionar el sólido y los parámetros de cada volumen.
    """
    Rta = input("ingrese el solido al que le quiere calcular su area prisma, piramide, cono o altura: ")

    if Rta== "prisma":
        area = int(input("ingrese el area de la base: "))
        altura = int(input("ingrese la altura: "))
        volumen =  area * altura
        print(f"El volumen del prisma es: {volumen}")

    elif Rta == "piramide":  
        area = int(input("ingrese el area de la base: "))
        altura = int(input("ingrese la altura: ")) 
        volumen = (1/3) * area * altura
        print(f"El volumen dela ítamide es: {volumen} ")

    elif Rta == "cono":   
        altura = int(input("ingrese la altura: "))
        radioBaseMayor = int(input("ingrese el radio de la base mayor: "))
        radioBaseMenor = int(input("ingrese el radio de la base menor: "))
        volumen = (1/3) * 3.14 * altura * (radioBaseMayor**2 + radioBaseMenor**2 + radioBaseMayor*radioBaseMenor)
        print(f"El volumen del cono es: {volumen}")

    elif Rta == "cilindro":
        base = int(input("ingrese la base: ")) 
        altura = int(input("ingrese la altura: ")) 
        volumen = base * altura
        print(f"El volumen del cilindro es: {volumen}")
elif menu == 4:        
    """
    4) Realice un programa que le permita al usuario escoger entre robot Cilíndrico, Cartesiano y esférico,
    donde como respuesta a la selección conteste con el tipo y número de articulaciones que posee.
    """
    robot = int(input("escoga un tipo de robot \n 1) cilindrico \n 2)cartesiano \n 3)esferico \n"))

    if robot == 1:
        print(" Tipo de articulaciones: Rotación (θ) Extensión (r) Elevación (z) \n Número de articulaciones: 3")
    elif robot == 2:
        print(" Tipo de articulaciones: Prismáticas (P) \n Número de articulaciones: 3 ")
    elif robot == 3:
        print(" Tipo de articulaciones: Rotación (θ, φ) Extensión (r) y Prismáticas (P) \n Número de articulaciones: 3") 
    else:          
        print("no selecciono ninguna opcion valida")

elif menu == 5:
    """
    5) Escribir un programa que realice la pregunta ¿Desea continuar Si/No? y que no deje de hacerla
    hasta que el usuario teclee No.
    """    
    pregunta = "si"
    while pregunta == "si":
        pregunta = input("desea continuar si/no: ")







