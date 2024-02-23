import numpy as np 
import math
"""
1)Realice un programa que sume, reste, multiplique (producto punto y producto cruz) y divida dos
vectores previamente inicializados.

"""

vector1 = np.array([4, 9, 8])
vector2 = np.array([6, 7, 8])

sumaVector = vector1 + vector2
restaVector = vector1 - vector2
productoPuntoVector = vector1 * vector2
productoCruzVector = np.cross(vector1, vector2)

print("\n la suma de los vectores es =",sumaVector,"\n la resta de los vectores es =", restaVector, "\n el prodcuto punto de los vectores es =", productoPuntoVector, "\n porducto crus de dos vectores es = ", productoCruzVector)

"""
2)Realice un programa que sume, reste, multiplique (producto punto y producto cruz) y divida dos
matrices previamente inicializadas.
"""
matriz1 = np.array([[1, 2, 5],[5, 6, 8]])
matriz2 = np.array([[4, 9, 8],[3, 2, 7]])

sumaMatrizes = matriz1 + matriz2
restaMatrizes = matriz1 - matriz2
productoPuntoMatrizes = matriz1 * matriz2

print("la suma de matrizes es = ", sumaMatrizes, "\n la resta de matrizes es = ", restaMatrizes, "\n el producto punto de las matrizes es = ", productoPuntoMatrizes)


"""
 3) Convierte coordenadas rectangulares a cilíndricas y esféricas
  Retorna Un diccionario con las coordenadas cilíndricas y esféricas

  """

def convertirCoordenadasRectangulares(x, y, z):
  
  # Coordenadas cilíndricas
  rho = (x**2 + y**2)**0.5
  theta = math.atan2(y, x)
  zCilindrica = z

  # Coordenadas esféricas
  rhoEsferica = (x**2 + y**2 + z**2)**0.5   
  thetaEsferica = theta
  phiEsferica = math.acos(z / rhoEsferica)

  return {
      "cilindricas": {"rho": rho, "theta": theta, "z": zCilindrica},
      "esfericas": {"rho": rhoEsferica, "theta": thetaEsferica, "phi": phiEsferica},
  }

coordenadasConvertidas = convertirCoordenadasRectangulares(2, 4, 3)
print(f"Coordenadas convertidas {coordenadasConvertidas}")




"""
4) calculo temperatura a partir de la resistencia de un sensor PT100

"""
# define la resistencia del sensor a 0°C
Resistencia = 100
alfa = 0.003926
resistenciaMedida = 138.5

temperatura = (resistenciaMedida - Resistencia) / (alfa * Resistencia)
print("La temperatura es:", temperatura, " grados C")

"""
5) funciones con maatrize de rotacion 

"""

def rotacionEnX(angulo):
  
  matriz = [[1, 0, 0], [0, math.cos(angulo), -math.sin(angulo)], [0, math.sin(angulo), math.cos(angulo)]]
  return matriz

def rotacionEnY(angulo):
  
  matriz = [[math.cos(angulo), 0, math.sin(angulo)], [0, 1, 0], [-math.sin(angulo), 0, math.cos(angulo)]]
  return matriz

def rotacionEnZ(angulo):
 
  matriz = [[math.cos(angulo), -math.sin(angulo), 0], [math.sin(angulo), math.cos(angulo), 0], [0, 0, 1]]
  return matriz

angulo = math.pi / 3
matrizX = rotacionEnX(angulo)
matrizY = rotacionEnY(angulo)
matrizZ = rotacionEnZ(angulo)

print("matriz de rotacion en X:", matrizX)
print("matriz de rotacion en Y:", matrizY)
print("matriz de rotacion en Z:", matrizZ)

"""
6)Calcula la fuerza de avance y retroceso de un cilindro neumático de doble efecto.
    Parámetros:
    presion: Presión de aire en el cilindro (Pa).
    diametro: Diámetro del cilindro (m).
    carrera: Carrera del cilindro (m).
"""
presion = 100000  
diametro = 0.1  
carrera = 0.2  


def FuerzaAvance(presion, diametro, carrera):
  
  area = math.pi * (diametro / 2)**2
  fuerza = area * presion
  return fuerza

def fuerzaRetroceso(presion, diametro):
 
  areaVastago = math.pi * (diametro / 2)**2
  fuerzaRetroceso = areaVastago * presion
  return fuerzaRetroceso


fuerzaAvance = FuerzaAvance(presion, diametro, carrera)
fuerzaRetroceso = fuerzaRetroceso(presion, diametro)

print("fuerza de avance: ", fuerzaAvance)
print("fuerza de retroceso: ", fuerzaRetroceso)