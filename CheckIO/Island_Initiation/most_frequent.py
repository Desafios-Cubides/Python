"""The most frequent (https://py.checkio.org/en/mission/the-most-frequent/)
You have a sequence of strings, and you’d like to determine the most frequently 
occurring string in the sequence. It can be the only one.

Input: Non-empty list of string (str).

Output: A string (str).
"""

def most_frequent(lista):
    frequent = {}
    
    for i in lista:
        if i in frequent:
            frequent[i] += 1
        else:
            frequent[i] = 1
            
    claves = list(frequent.keys())
    valor = list(frequent.values())
    
    valor_maximo = max(valor)
    indice_valor_maximo = valor.index(valor_maximo)
    valor_frecuente = claves[indice_valor_maximo]
    
    print(valor_frecuente)
        

lista = ["a", "b", "a", "c", "b", "b"]
most_frequent(lista)