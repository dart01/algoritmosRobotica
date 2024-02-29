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
radio = 0.1  
carrera = 0.2  


def fuerzaAvance(presion, radio ):
  
  superficie = math.pi * (radio**2)
  fuerza = superficie * presion
  return fuerza

def fuerzaRetroceso(presion, radio, carrera):
 
  areaVastago = math.pi * ((radio**2)*(carrera**2))
  fuerzaRetroceso = areaVastago * presion
  return fuerzaRetroceso


fuerzaAvance = fuerzaAvance(presion, radio)
fuerzaRetroceso = fuerzaRetroceso(presion, radio, carrera)

print("fuerza de avance: ", fuerzaAvance, "N")
print("fuerza de retroceso: ", fuerzaRetroceso ,"N")