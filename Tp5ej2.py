#################
#Mateo2021-icomp
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Fibonacci

def prueba():
    num_uno, num_dos = 0, 1 
    while num_dos <= 2500:
        print(num_uno, num_dos, end=" ")
        num_uno = num_uno + num_dos
        num_dos = num_uno + num_dos

if __name__ == "__main__":
    prueba()