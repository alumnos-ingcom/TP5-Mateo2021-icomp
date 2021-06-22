#################
#Mateo2021-icomp
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Numeros Capicua

import math
def prueba():
    numero = int(input("Ingrese un numero: "))
    numerodedigitos = int(math.log10(numero))+1
    numero1 = numero
    digito = 0
    numerocapicua = 0
    for i in range(numerodedigitos):
        digito = numero % 10
        numero = numero //10 
        numerocapicua = numerocapicua*10+digito
    print(numero1)
    print(numerocapicua)
    if numero1 == numerocapicua:
        print("El numero es capicua: ")
    else:
        print("El numero no es capicua: ")
    print (prueba())


if __name__ == "__main__":
    prueba()