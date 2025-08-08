""" Enunciado
You should return a given string in reverse order.

Input: A string (str).

Output: A string (str).

Examples:
assert backward_string("val") == "lav"
assert backward_string("") == ""
assert backward_string("ohho") == "ohho"
assert backward_string("123456789") == "987654321"
"""

def backward_string(palabra):
    palabra_nueva = "" # Nueva palabra
    
    for i in range(0, len(palabra)):
        """con esta función obtenemos una nueva palabra de
        forma invertida
        """
        valor_indice = palabra[(len(palabra) - 1) - i]
        palabra_nueva += valor_indice
    
    return palabra_nueva

entrada = input("Ingrese una plabra: ")
p_invertida = backward_string(entrada)
print(p_invertida)