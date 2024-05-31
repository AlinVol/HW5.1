import string
import keyword


def is_valid_variable_name(variable_name):
    if variable_name in keyword.kwlist:
        return False

    if variable_name[0].isdigit():
        return False

    for char in variable_name:
        if char.isupper():
            return False
        if char in string.punctuation and char != '_':
            return False
        if char == ' ':
            return False

    if variable_name.count('_') > 1:
        return False

    return True


variable_name = input("Enter a variable name: ")
print(is_valid_variable_name(variable_name))