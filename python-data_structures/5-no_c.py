#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for i in my_string:
        if i != "c" and i != "C":  # Vérifie que i n'est ni 'c' ni 'C'
            new_string += i         # Ajoute le caractère à la nouvelle chaîne
    return new_string

