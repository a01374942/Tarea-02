#encoding: UTF-8

# Autor: Angel Roberto Pesado Bartolo, A01374942
# Descripcion: Realizaré un programa que imprima el porcentaje de mujeres y hombres que hay en una clase, dado por el usuario.

# A partir de aquí escribe tu programa

hombres = int(input("Dame el numero de hombres dentro de la clase: "))
mujeres = int(input("Dame el numero de mujeres dentro de la clase: "))
totala = (hombres + mujeres)
porcentajeh = (100*hombres)/(totala)
porcentajem = (100*mujeres)/(totala)
print("El total de alumnos en clase es de: ",totala,"alumnos")
print("El porcentaje de hombres es de:",porcentajeh,"%")
print("El porcentaje de mujeres es de:",porcentajem,"%")
