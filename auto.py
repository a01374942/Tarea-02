#encoding: UTF-8

# Autor:Angel Roberto Pesado Bartolo, A01374942
# Descripcion: Pedir al usuario la velocidad de un auto e indicar cuanta distancia recorre en 6 y 10 horas, además de indicar cuanto tiempo tarda en recorrer 500km

# A partir de aquí escribe tu programa


velocidad=float(input("Dame la velocidad del auto: "))
hora=velocidad*6
hora2=velocidad*10
distancia= 500/velocidad
print("Tu distancia en 6 horas es: ",hora,"km")
print("Tu distancia en 10 horas es: ",hora2,"km")
print("En este tiempo recorreras 500 km: ",distancia,"horas")