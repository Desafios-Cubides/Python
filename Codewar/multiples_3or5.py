""""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the 
number passed in. Additionally, if the number is negative, return 0 
(for languages that do have them).

Note: If the number is a multiple of both 3 and 5, only count it once.

"""

# Devolver la suma de todos los múltiplos de 3 o 5 debajo de (n) → n=6 == 3 y 5.
# Si el número es negativo, devuelve 0.
# Devolver la suma de los números.

def solution(number):
 # Se calcula los multiplos de 3 or 5 y se devuelve la suma de la adición de estos.
    if (number < 0):
        return 0
    else:
        a= 0
        for i in range(1, number):
            if (i%5 == 0 or i%3 == 0):
                a+= i
    return a

print(solution(10))


"""" zyxwhut
def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)
"""

"""" dendazen
def solution(number):
    sum = 0
    for i in range(number):
        if (i % 3) == 0 or (i % 5) == 0:
            sum += i
    return sum
"""