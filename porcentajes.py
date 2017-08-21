#encoding: UTF-8

# Autor: Angel Roberto Pesado Bartolo, A01374942
# Descripcion: Realizaré un programa que imprima el porcentaje de mujeres y hombres que hay en una clase, dado por el usuario.

# A partir de aquí escribe tu programa

hombres = int(input("Dame el numero de hombres dentro de la clase: "))
mujeres = int(input("Dame el numero de mujeres dentro de la clase: "))
total = (hombres + mujeres)
porcentajeh = (100*hombres)/(total)
porcentajem = (100*mujeres)/(total)
print("El total de alumnos en clase es de: ",total,"alumnos")
print("El porcentaje de hombres es de:",porcentajeh,"%")
print("El porcentaje de mujeres es de:",porcentajem,"%")
