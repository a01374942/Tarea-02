#encoding: UTF-8


# Autor:Angel Roberto Pesado Bartolo, A01374942
# Descripcion: Elaborar un algoritmo que pida al usuario las coordenadas de un punto y obtener el angulo y la magnitud.

# A partir de aquí escribe tu programa

import math

x=float(input("Dame el valor en x: "))
y=float(input("Dame el valor en y: "))
angR = math.atan2(y,x)
angT = (angR*180)/(3.1416)
magnitud= math.sqrt(x**2+y**2)
print("La magnitud es de ",magnitud)
print("El angulo que se forma es de ", angT)
