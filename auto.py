#encoding: UTF-8

# Autor:Angel Roberto Pesado Bartolo, A01374942
# Descripcion: Pedir al usuario la velocidad de un auto e indicar cuanta distancia recorre en 6 y 10 horas, además de indicar cuanto tiempo tarda en recorrer 500km

# A partir de aquí escribe tu programa

a=float(input("Dame la velocidad del auto: "))
b= a*6
print("Tu distancia en 6 horas es: ",b,"km")
c= a*10
d= 500/a
print("Tu distancia en 10 horas es: ",c,"km")
print("En este tiempo recorreras 500 km: ",d,"horas")