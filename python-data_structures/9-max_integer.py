#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_var = my_list[0]
    for i in my_list:
        if i > max_var:
            max_var = i
    return max_var
