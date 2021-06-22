#################
#Mateo2021-icomp
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Busqueda de palabras

def prueba():
        import re
        frase = str(input("Ingrese una palabra o texto: "))
        palabra = str(input("ingrese la palabra a buscar: "))
        try:
            resultado = re.search(palabra, frase)
            inicio = resultado.start()
            final = resultado.end()
            print ("La palabra {} se encontro al inicio {} y final {}: ".format(palabra, inicio, final))
        except:
            print("La palabra no estaba en el texto: ")
        pass


if __name__ == "__main__":
    prueba()


