#################
#Mateo2021-icomp
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Numeros Perfectos

def prueba():
    def NumeroPerfecto(num):
      suma = 0
      for i in range(1,num):
        if (num % i == 0):
          suma += i

      if num == suma:
        return True
      else:
        return False

    num = int(input("introduzca un numero:"))

    if NumeroPerfecto(num):
      print("%s es un numero perfecto" % num)
    else:
      print("%s NO es un numero perfecto" % num)
      pass

if __name__ == "__main__":
    prueba()
        
    