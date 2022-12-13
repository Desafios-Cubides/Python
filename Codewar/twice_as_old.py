""" DEFINICIÓN PROBLEMA
Your function takes two arguments:

Current father's age (years)

Current age of his son (years)

Сalculate how many years ago the father was twice as old as his 
son (or in how many years he will be twice as old).


----------------------------------------------------------------
EXAMPLE:

Entrada:
father= 55
son= 30

Salida:
Hace 5 años el father tenia el doble de la edad del son.
father= 50
son= 25

50/2= 25 (son)
25*2= 50 (father)
"""

""" Unnamed
def twice_as_old(dad_years_old, son_years_old):
    return abs(dad_years_old - 2*son_years_old)

dad= [45, 67, 89, 50]
son= [20, 33, 45, 23]

for i in range(len(dad)):
    print(twice_as_old(dad[i], son[i]))
"""

""" elias-ela
def twice_as_old(dad_years_old, son_years_old):
    count = 0
    if son_years_old == 0:
        return dad_years_old
    elif dad_years_old / son_years_old > 2:
        while son_years_old * 2 != dad_years_old:
            dad_years_old += 1
            son_years_old += 1
            count += 1
        return count
    elif dad_years_old / son_years_old < 2:
        while son_years_old != 0 and son_years_old * 2 != dad_years_old:
            dad_years_old -= 1
            son_years_old -= 1
            count += 1
        return count
    else:
        return 0

print(twice_as_old(45, 20))
print(twice_as_old(67, 33))
"""