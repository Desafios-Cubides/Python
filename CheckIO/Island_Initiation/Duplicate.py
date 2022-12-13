""" Duplicate Zeros https://py.checkio.org/en/mission/duplicate-zeros/
Sometimes, zeros resemble very tasty donuts. And every time we finish a donut, we want 
another, and then another, and then another..."

You are given a list of integers. Your task in this mission is to double all the zeros 
in the given list (think about donuts ;-P).

Input: List.

Output: List.

Example:

assert duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0]) == [1, 0, 0, 2, 3, 0, 0, 4, 5, 0, 0]
assert duplicate_zeros([0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0, 0, 0]
assert duplicate_zeros([100, 10, 0, 101, 1000]) == [100, 10, 0, 0, 101, 1000]
1
2
3

If you have solved this mission, you can enjoy a donut with peace of mind!=)
"""

"""
def duplicate_zeros(list):
    count = 0

    while(count <= len(list)):
        for i in list:
            if(list[count] == 0):
                list.insert(count, 0)
                
                if (count == len(list)):
                    break
                else:
                    count += 2

                print(list)
            else:
                count += 1

    return "Hola"
"""

def duplicate_zeros(list):
    """
    The function searches a list for a set of 0 and then adds them near the same position 
    where that data was found.

    A counter is used to use it in the path instead of the same for variable (i), this 
    so that when a 0 is added it increases by 2 and if it does not find a two it increases 
    by 1.

    If we use the range function with the len function in the entered list, then this value 
    will remain constant and will not be modified when adding new elements.
    """

    count = 0

    for i in range(0, len(list)):
        if(list[count] == 0):
            list.insert(count, 0)
            count += 2
        else:
            count += 1
    
    return list


print("Example:")
print("________________________________________________________")
print(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0]))
print(duplicate_zeros([0, 0, 0, 0]))
print(duplicate_zeros([100, 10, 0, 101, 1000]))

print("The mission is done! Click 'Check Solution' to earn rewards!")