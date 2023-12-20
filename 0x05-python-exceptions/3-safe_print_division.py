#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        res = a / b
    except ZeroDivisionError:
        res = None
    finally:
        print("Inside result: {:f}".format(res))

a = 5
b = 0
result = safe_print_division(a, b)
