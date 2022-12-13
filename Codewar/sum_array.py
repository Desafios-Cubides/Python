""""
Write a function that takes an array of numbers and returns the sum of the numbers. 
The numbers can be negative or non-integer. If the array does not contain any 
numbers then you should return 0.

Examples
Input: [1, 5.2, 4, 0, -1]
Output: 9.2

Input: []
Output: 0

Input: [-2.398]
Output: -2.398

Assumptions
You can assume that you are only given numbers.
You cannot assume the size of the array.
You can assume that you do get an array and if the array is empty, return 0.
What We're Testing
We're testing basic loops and math operations. This is for beginners who are just 
learning loops and math operations.
Advanced users may find this extremely easy and can easily write this in one line.

"""

# Datos de entrada: int, float
# Almacenar datos de entrada en un array
# Datos de salida: suma de números del array
 
#### Solución

"""" JoeWalters
def sum_array(a):
    total = 0
    i = 0
    while i < len(a):
        total += a[i]
        i += 1
    return total

a= [6, 8.9]
print(sum_array(a))
"""

""" FullOfBologna
def sum_array(a):
    sum = 0
    for i in a:
        sum += i
    return sum

a= [5, 9.32, 2]
print(sum_array(a))
"""

# Yo
a= [8, 7, 9.0]

def sum_array(a):
    """"
    suma= 0
    suma+= a[0] + a[1] + a[2] + a[3]
    return suma
    """
    b= 0
    for i in range(len(a)):
        b+= a[i]
    return b

print(sum_array(a))
