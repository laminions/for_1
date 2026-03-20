cantidad_pares = 0
cantidad_impares = 0
lista_numeros = "numeros: "

for i in range (1, 21):
    n = int (input("dijite el numero" + str(i) + ":"))

    lista_numero = lista_numero + str (n) + ","
    m = n%2

    if (m == 0):
        cantidad_pares = cantidad_pares +1
    else:
        cantidad_impares = cantidad_impares +1

# output

print("El total de numeros pares es: ", cantidad_pares)
print("El total de numeros impares es: " , cantidad_impares)


