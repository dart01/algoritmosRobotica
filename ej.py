import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
import control.matlab as control

# k = float(input("Ingrese la ganancia estática (K): "))
# wn = float(input("Ingrese la frecuencia natural no amortiguada (ωn): "))
# zita = float(input("Ingrese el factor de amortiguamiento (ζ): "))

# Rta = control.TransferFunction([k],[1., zita, wn])
# print(Rta)

# if zita < 1 :
#     print("sistema subamortiguado")
# elif zita == 1 :
#     print("sistema amortiguado")
# elif zita < 1 :
#     print("sistema sobreamortiguado")
       
# y,t = control.step(Rta)
# plt.plot(t,y)
# plt.xlabel('Tiempo')
# plt.title("Respuesta de sistema segundo Orden")
# plt.show()
import matplotlib.pyplot as plt

# Function to draw the letter D
def D(ax):
    ax.plot([0.5, 0.5], [1, 5], color='black')
    ax.plot([0.5, 2.5], [5, 5], color='black')
    ax.plot([0.5, 2.5], [1, 1], color='black')
    ax.plot([2.6, 2.6], [4.7, 1.3], color='black')
    ax.plot([2.5, 2.6], [1, 1.3], color='black')
    ax.plot([2.5, 2.6], [5, 4.7], color='black')
# Function to draw the letter I
def I(ax):
    ax.plot([3, 3], [1, 5], color='black')

# Function to draw the letter E
def E(ax):
    ax.plot([3.5, 3.5], [1, 5], color='black')
    ax.plot([3.5, 5], [1, 1], color='black')
    ax.plot([3.5, 5], [5, 5], color='black')
    ax.plot([3.5, 5], [3, 3], color='black')
# Function to draw the letter G
def G(ax):
    ax.plot([5.5, 5.5], [1, 5], color='black')
    ax.plot([5.5, 7], [1, 1], color='black')
    ax.plot([5.5, 7], [5, 5], color='black')
    ax.plot([7, 7], [1, 3], color='black')
    ax.plot([7, 6], [3, 3], color='black')
# Function to draw the letter O
def O(ax):
    ax.plot([7.3, 7.3], [1, 5], color='black')
    ax.plot([7.3, 9], [1, 1], color='black')
    ax.plot([9, 9], [1, 5], color='black')
    ax.plot([7.3, 9], [5, 5], color='black')

# Main function to draw the name "Diego"
def main():
    fig, ax = plt.subplots(figsize=(7, 5))  # Set a larger figure size

    D(ax)
    I(ax)
    E(ax)
    G(ax)
    O(ax)
    # Adjust the axis limits to fit the letters comfortably
    ax.set_xlim(0, 12)  
    ax.set_ylim(0, 8)  

    ax.axis('off')  # Hide the axes

    plt.show()


main()