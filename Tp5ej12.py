#################
#Mateo2021-icomp
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Comparacion Listas

def prueba():
    numerodeveces= 3
    listauno = []
    listados = []
    for i in range (numerodeveces):
        listauno.append(input("Incerte los valores de la lista uno: "))
        listados.append(input("Incerte los  valores de la lista dos: "))
    if (set(listauno) == set (listados)):
        print ("True")
    else:
        print("False")
        
if __name__ == "__main__":
    prueba()