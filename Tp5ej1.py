#################
#Mateo2021-icomp
# UNRN Andina - Introducción a la Ingenieria en Computación
################


#Pares e Impares.

def prueba():
    numero = int(input("Ingrese el numero: "))
    numero = numero+1
    def is_even(numero):
        return (numero // 2) * 2 == numero
    def is_odd(numero):
        return not(is_even(numero))
    for numero in range(numero):
        print(f"{numero} {'True' if is_even(numero) else 'False'}")
        pass

if __name__ == "__main__":
    prueba()