
""" Mi programa
def are_you_playing_banjo(name):
    # Implement me!
    if(name[0] == "R" or name[0] == "r"):
        name1= f"{name} play banjo"
    else:
        name1= f"{name} does not play banjo"

    return name1
"""

""" Segundo programa
def areYouPlayingBanjo(name):
    return name + (' plays' if name[0].lower() == 'r' else ' does not play') + " banjo";
"""

# while True:
    # name= input("Ingrese un nombre: ")
    # print(are_you_playing_banjo(name))
    #print(areYouPlayingBanjo(name))

name1= input("bueno: ")    
print(name1[0].lower())