#################
#Mateo2021-icomp
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#Distancias

def prueba():
    numero = int(input("Ingrese un numero: "))
    numerodos = int(input("Ingrese un segundo numero: "))
    def distancia(numero):
        if numero >= 0:
            return numero
        else:
            return - numero
    def distancia(numerodos):
        if numerodos >= 0:
            return numerodos
        else:
            return - numerodos

    if numero == numerodos:
        print()
    if numero > 0 and numerodos < 0:
        print("La distancia entre los dos numeros es: ", numero + -numerodos)
    if numero < 0 and numerodos > 0:
        print("La distancia entre los dos numeros es: ", -numero + numerodos)
    if numero > 0 and numerodos > 0:
        if numero < numerodos:
            print("La distancia entre los dos numeros es: ", -numero + numerodos)
        else:
            print("La distancia entre los dos numeros es: ", numero - numerodos)
    if numero < 0 and numerodos < 0:
        if numero < numerodos:
            print("La distancia entre los dos numeros es: ", -numero + numerodos)
        else:
            print("La distancia entre los dos numeros es: ", numero - numerodos)
        print(prueba())

if __name__ == "__main__":
    prueba()