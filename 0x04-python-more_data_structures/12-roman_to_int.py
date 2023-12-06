#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    if not isinstance(roman_string, str):
        return 0
    if not check_input(roman_string):
        return 0
    result = convert_roman_to_int(roman_string)
    return result
