#################
#Mateo2021-icomp
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#Parentesis Balanceados

def prueba():
    def is_balanced(brackets, open_brackets="({[", close_brackets=")}]"):
        stack = []
        for bracket in brackets:
            if bracket in open_brackets:
                stack.append(bracket)
            elif len(stack) == 0:
                return False
            elif bracket in close_brackets:
                stacked = stack.pop()
                closed_bracket_position = close_brackets.index(bracket)
                open_bracket = open_brackets[closed_bracket_position]
                if stacked != open_bracket:
                    return False

        return not len(stack)


    def braces(values):
        response = []
        for string in values:
            if is_balanced(string):
                response.append(True)
            else:
                response.append(False)

        return response

    Ejemplo = ""
    Ejemplo1 = "[]"
    Ejemplo2 = "[][]"
    Ejemplo3 = "[[][]]"
    Ejemplo4= "]["
    Ejemplo5= "][]["
    Ejemplo6= "[]][[]"
    Ejemplos = [Ejemplo ,Ejemplo1 ,Ejemplo2 ,Ejemplo3 ,Ejemplo4 ,Ejemplo5 ,Ejemplo6]
    print(braces(Ejemplos))

if __name__ == "__main__":
    prueba()
