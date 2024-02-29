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