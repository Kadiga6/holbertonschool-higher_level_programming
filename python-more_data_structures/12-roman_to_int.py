#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    total = 0
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    for i in range(len(roman_string)):
        # Si ce n'est pas le dernier caractère et la valeur actuelle est inférieure à la suivante
        if i < len(roman_string) - 1 and roman_values[roman_string[i]] < roman_values[roman_string[i + 1]]:
            total -= roman_values[roman_string[i]]
        else:
            total += roman_values[roman_string[i]]

    return total
