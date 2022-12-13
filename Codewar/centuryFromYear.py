"""
Introduction
The first century spans from the year 1 up to and including 
the year 100, the second century - from the year 101 up to and 
including the year 200, etc.

Task
Given a year, return the century it is in.

Examples
1705 --> 18
1900 --> 19
1601 --> 17
2000 --> 20
"""

"""
import numpy as np

n= np.arange(500)

def century(ano):
    for i in range(len(n)):
        if (i < ano <= i*100):
            return f"El año: {ano} pertenece al Siglo: {i}"
        elif (i*100 < ano <=(i+1)*100):
            return f"El año: {ano} pertenece al Siglo: {i+1}"


print(century(1))
print(century(5200))
print(century(18955464))
"""


def century(ano):
    return int((ano/100)+1)

print(century(1984))
print(century(7800))
print(century(5987))
