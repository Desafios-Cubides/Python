""""" Mi programa
def even_or_odd(number):
    if(number%2 == 0):
        number1= f"{number} is Even"
    else:
        number1= f"{number} is Odd"
    return number1
"""""

""""" Segundo programa (alder)
def even_or_odd(number):
  return ["Even", "Odd"][number % 2]
"""""

""""" Tercer programa (ksolademi)
def even_or_odd(number):
    return 'Odd' if number % 2 else 'Even'
"""""

"""""
while True:
    number= int(input("Ingrese un número: "))
    print(even_or_odd(number))
"""
