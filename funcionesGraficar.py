import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate

seleccion = int(input("ingrese su opcion: "))
if seleccion == 1:



# Se calcula la temperatura
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


elif seleccion ==2 : 
    """
    2)Realice un programa que le permita al usuario ingresar los coeficientes de una función de
    transferencia de segundo orden y graficar su comportamiento, además se debe mostrar que tipo
    de sistema es: subamortiguado, criticamente amortiguado y sobreamortiguado."""

    def funcionTransferencia():
        # Ingreso de coeficientes
        K = float(input("Ingrese la ganancia estática (K): "))
        wn = float(input("Ingrese la frecuencia natural no amortiguada (ω_n): "))
        zeta = float(input("Ingrese el factor de amortiguamiento (ζ): "))

        #  del rango de tiempo
        t = np.linspace(0, 10, 1000)

        if zeta < 1:
            # Sistema subamortiguado
            print("Sistema subamortiguado")
            y = K * wn * np.exp(-zeta * wn * t) * np.sin(wn * np.sqrt(1 - zeta**2) * t) / np.sqrt(1 - zeta**2)
        elif zeta == 1:
            # Sistema críticamente amortiguado
            print("Sistema críticamente amortiguado")
            y = K * wn * t * np.exp(-zeta * wn * t)
        else:
            # Sistema sobreamortiguado
            print("Sistema sobreamortiguado")
            y = K * (1 - (zeta + np.sqrt(zeta**2 - 1)) * np.exp(-(zeta + np.sqrt(zeta**2 - 1)) * wn * t) +
                    (zeta - np.sqrt(zeta**2 - 1)) * np.exp(-(zeta - np.sqrt(zeta**2 - 1)) * wn * t))

        # Graficación de la respuesta
        plt.plot(t, y, label="Respuesta del sistema")
        plt.xlabel("Tiempo")
        plt.ylabel("Salida del sistema")
        plt.legend()
        plt.show()
    funcionTransferencia()

elif seleccion== 3:

    funcionTransferencia()
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

    """
    4) Consulte y elabore un sistema coordenado X, Y y Z donde se dibuje un vector con coordenadas
    ingresadas por el usuario.
    """