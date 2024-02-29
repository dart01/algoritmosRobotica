import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
import control.matlab as control
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch

seleccion = int(input("ingrese su opcion \n 1) calcular temperatura: \n 2) funcion de transferencia: \n 3) carga y descarga circuito RC: \n 4)sistema coordenado X, Y y Z donde se dibuje un vector: \n 5) nombre de los integrantes del grupo en un plot en 2D: "))
if seleccion == 1:



# Se calcula la temperatura
    temperature = 26
    r0 = 100
    a = 0.00385
    b = 0.0000025
    def temperaturaRtd(temperatura, r0, a, b):
        """
        temperature: La temperatura en °C.
        r0: La resistencia del RTD a 0°C en ohmios.
        a: Coeficiente de temperatura del RTD a 0°C en °C⁻¹.
        b: Coeficiente de temperatura cuadrático del RTD en °C⁻².
        """
        return r0 * (1 + a * temperatura + b * temperatura**2)

    resistancia = temperaturaRtd(temperature, r0, a, b)
    print(f"La resistencia del RTD es de {resistancia} Ω")


elif seleccion ==2 : 
    """
    2)Realice un programa que le permita al usuario ingresar los coeficientes de una función de
    transferencia de segundo orden y graficar su comportamiento, además se debe mostrar que tipo
    de sistema es: subamortiguado, criticamente amortiguado y sobreamortiguado."""

    k = float(input("Ingrese la ganancia estática (K): "))
    wn = float(input("Ingrese la frecuencia natural no amortiguada (ωn): "))
    zita = float(input("Ingrese el factor de amortiguamiento (ζ): "))

    Rta = control.TransferFunction([k],[1., zita, wn])
    print(Rta)

    if zita < 1 :
        print("sistema subamortiguado")
    elif zita == 1 :
        print("sistema amortiguado")
    elif zita < 1 :
        print("sistema sobreamortiguado")
        
    y,t = control.step(Rta)
    plt.plot(t,y)
    plt.xlabel('Tiempo')
    plt.title("Respuesta de sistema segundo Orden")
    plt.show()

elif seleccion== 3:


    """
    3)Implemente la ecuación de carga y descarga para un circuito RC. El usuario ingresa por teclado el
    valor de voltaje (V), capacitancia (μF) y resistencia (Ω).
    """
    voltaje = float(input("Ingrese el voltaje: "))
    capacitancia = float(input("Ingrese la capacitancia: "))
    resistencia = float(input("Ingrese la resistencia: "))

    t = np.linspace(0, 1, 100)  # Rango de tiempo
    integral = np.log(np.abs(t)) / (capacitancia * resistencia)

    plt.plot(t, integral)
    plt.xlabel("Tiempo")
    plt.ylabel("Valor integral")
    plt.show()

elif seleccion== 4:    
    """
    4) Consulte y elabore un sistema coordenado X, Y y Z donde se dibuje un vector con coordenadas
    ingresadas por el usuario.
    """
    def dibujarVector(x, y, z):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        ax.quiver(0, 0, 0, 1, 0, 0, color='black', arrow_length_ratio=0.1)
        ax.quiver(0, 0, 0, 0, 1, 0, color='red', arrow_length_ratio=0.1)
        ax.quiver(0, 0, 0, 0, 0, 1, color='blue', arrow_length_ratio=0.1)

        ax.quiver(0, 0, 0, x, y, z, color='black', arrow_length_ratio=0.1)

        ax.set_xlim([-1, 1])
        ax.set_ylim([-1, 1])
        ax.set_zlim([-1, 1])
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('Vector en un sistema de coordenadas tridimensional')

        plt.show()

    def vector():
        X = float(input("INGRESE LA COORDENADA X DEL VECTOR A DIBUJAR: "))
        Y = float(input("INGRESE LA COORDENADA Y DEL VECTOR A DIBUJAR: "))
        Z = float(input("INGRESE LA COORDENADA Z DEL VECTOR A DIBUJAR: "))

        dibujarVector(X, Y, Z)

    vector()

elif seleccion== 5:
    """
    Dibuje el nombre de cada uno de los integrantes del grupo en un plot en 2D, teniendo en cuenta
    líneas rectas y/o curvas.
    """   
    def D(ax):
        ax.plot([0.5, 0.5], [1, 5], color='black')
        ax.plot([0.5, 2.5], [5, 5], color='black')
        ax.plot([0.5, 2.5], [1, 1], color='black')
        ax.plot([2.6, 2.6], [4.7, 1.3], color='black')
        ax.plot([2.5, 2.6], [1, 1.3], color='black')
        ax.plot([2.5, 2.6], [5, 4.7], color='black')

    def I(ax):
        ax.plot([3, 3], [1, 5], color='black')

    def E(ax):
        ax.plot([3.5, 3.5], [1, 5], color='black')
        ax.plot([3.5, 5], [1, 1], color='black')
        ax.plot([3.5, 5], [5, 5], color='black')
        ax.plot([3.5, 5], [3, 3], color='black')

    def G(ax):
        ax.plot([5.5, 5.5], [1, 5], color='black')
        ax.plot([5.5, 7], [1, 1], color='black')
        ax.plot([5.5, 7], [5, 5], color='black')
        ax.plot([7, 7], [1, 3], color='black')
        ax.plot([7, 6], [3, 3], color='black')
   
    def O(ax):
        ax.plot([7.3, 7.3], [1, 5], color='black')
        ax.plot([7.3, 9], [1, 1], color='black')
        ax.plot([9, 9], [1, 5], color='black')
        ax.plot([7.3, 9], [5, 5], color='black')

    #  "Diego"
    def main():
        fig, ax = plt.subplots(figsize=(7, 5))  # Set a larger figure size

        D(ax)
        I(ax)
        E(ax)
        G(ax)
        O(ax)
        
        ax.set_xlim(0, 12)  
        ax.set_ylim(0, 8)  
        ax.axis('off')  
        plt.show()

    main()
