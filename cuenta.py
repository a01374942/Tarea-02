#encoding: UTF-8

# Autor: Angel Roberto Pesado Bartolo, A01374942
# Descripcion: Primero debemos pedir al usuario el gastó para después obtener la iva y la propina, para finalmente imprimir el gasto total..

# A partir de aquí escribe tu programa

subtotal=float(input("Dime cuanto gastaste en el restarurante: "))
propina=(subtotal*.12)
iva= (subtotal*.16)
total= (subtotal+propina+iva)
print("Tu subtotal es de: ",subtotal,"pesos")
print("Tu propina a pagar es:",propina,"pesos")
print("Tu IVA a pagar es de: ",iva,"pesos")
print("Tu TOTAL a pagar es de ",total,"pesos")