"""
def first_word(str):
    word= str
    only= ""

    for i in range(0, len(word)):
        if word[i] == " ":
            only= word[0 : i]
            break

    return only
"""

# Consiste en imprimir la palabra que esta antes del primer espacio (" ")
def first_word(str):
    word= str.split()

    return word[0]


print("Example:")
print(first_word("greeting from CheckiO Planet"))