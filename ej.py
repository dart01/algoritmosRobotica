# Rta = input("ingrese el solido al que le quiere calcular su area: ")

# if Rta== "prisma":
#      area = int(input("ingrese el area de la base: "))
#      altura = int(input("ingrese la altura: "))
#      volumen =  area * altura
#      print(f"El volumen del prisma es: {volumen}")

# elif Rta == "piramide":  
#      area = int(input("ingrese el area de la base: "))
#      altura = int(input("ingrese la altura: ")) 
#      volumen = (1/3) * area * altura
#      print(f"El volumen dela ítamide es: {volumen} ")

# elif Rta == "cono":   
#       altura = int(input("ingrese la altura: "))
#       radioBaseMayor = int(input("ingrese el radio de la base mayor: "))
#       radioBaseMenor = int(input("ingrese el radio de la base menor: "))
#       volumen = (1/3) * 3.14 * altura * (radioBaseMayor**2 + radioBaseMenor**2 + radioBaseMayor*radioBaseMenor)
#       print(f"El volumen del cono es: {volumen}")

# elif Rta == "cilindro":
#      base = int(input("ingrese la base: ")) 
#      altura = int(input("ingrese la altura: ")) 
#      volumen = base * altura
#      print(f"El volumen del cilindro es: {volumen}"




# robot = int(input("escoga un tipo de robot \n 1) cilindrico \n 2)cartesiano \n 3)esferico \n"))

# if robot == 1:
#     print(" Tipo de articulaciones: Revolucionarias (R) \n Número de articulaciones: 3")
# elif robot == 2:
#     print(" Tipo de articulaciones: Prismáticas (P) \n Número de articulaciones: 3 ")
# elif robot == 3:
#     print(" Tipo de articulaciones: Revolucionarias (R) y Prismáticas (P) \n Número de articulaciones: 3 o 4") 
# else:          
#     print("no selecciono ninguna opcion valida")
# pregunta = "si"
# while pregunta == "si":
#     pregunta = input("desea continuar si/no: ")








# import matplotlib.pyplot as plt
# import numpy as np
# def main():
#     # Ingreso de coeficientes
#     K = float(input("Ingrese la ganancia estática (K): "))
#     wn = float(input("Ingrese la frecuencia natural no amortiguada (ω_n): "))
#     zeta = float(input("Ingrese el factor de amortiguamiento (ζ): "))

#     # Cálculo de polos
#     s1 = -zeta * wn + np.sqrt(zeta**2 * wn**2 - wn**2)
#     s2 = -zeta * wn - np.sqrt(zeta**2 * wn**2 - wn**2)

#     # Definición del rango de tiempo
#     t = np.linspace(0, 10, 1000)

#     # Cálculo de la respuesta
#     if zeta < 1:
#         # Sistema subamortiguado
#         y = K * wn * np.exp(-zeta * wn * t) * np.sin(wn * np.sqrt(1 - zeta**2) * t) / np.sqrt(1 - zeta**2)
#     elif zeta == 1:
#         # Sistema críticamente amortiguado
#         y = K * wn * t * np.exp(-zeta * wn * t)
#     else:
#         # Sistema sobreamortiguado
#         y = K * (1 - (zeta + np.sqrt(zeta**2 - 1)) * np.exp(-(zeta + np.sqrt(zeta**2 - 1)) * wn * t) +
#                   (zeta - np.sqrt(zeta**2 - 1)) * np.exp(-(zeta - np.sqrt(zeta**2 - 1)) * wn * t))

#     # Graficación de la respuesta
#     plt.plot(t, y, label="Respuesta del sistema")
#     plt.xlabel("Tiempo (t)")
#     plt.ylabel("Salida del sistema (y)")
#     plt.legend()
#     plt.show()

#     # Determinación del tipo de sistema
#     if zeta < 1:
#         print("Sistema subamortiguado")
#     elif zeta == 1:
#         print("Sistema críticamente amortiguado")
#     else:
#         print("Sistema sobreamortiguado")

# main()
# }





# import sympy as sym
# from scipy import integrate
# # Definir la variable simbólica
# x = sym.Symbol('x')

# # Definir la función a integrar
# f = x**2

# # Calcular la integral
# integral = sym.integrate(f, x)

# # Mostrar el resultado
# print(integral)




# import numpy as np

# # Definir matrices
# matriz_a = np.array([[1, 2, 3], [4, 5, 6]])
# matriz_b = np.array([[7, 8, 9], [10, 11, 12]])

# # Suma elemento a elemento
# suma = matriz_a + matriz_b

# # Imprimir el resultado
# print("Suma elemento a elemento:\n", suma)

# import numpy as np
# import matplotlib.pyplot as plt 

# voltaje = float(input("Ingrese el voltaje: "))
# capacitancia = float(input("Ingrese la capacitancia: "))
# resistencia = float(input("Ingrese la resistencia: "))

# t = np.linspace(0, 1, 100)  # Rango de tiempo
# integral = np.log(np.abs(t)) / (capacitancia * resistencia)

# plt.plot(t, integral)
# plt.xlabel("Tiempo")
# plt.ylabel("Valor integral")
# plt.show()

import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

rMedida= 100
Resistencia = 500
alfa= 50
temperatura = (rMedida - Resistencia) / (alfa * Resistencia)
x= np.array([-200, -100, 0, 100, 200])
y = np.array([38.5, 264.9, 100, 138.5, 264.9])
plt.plot(x, y)
plt.title("coportamiento PT100 de -200 a 200")
plt.xlabel("temperatura")
plt.ylabel("resistencia")
plt.show()
