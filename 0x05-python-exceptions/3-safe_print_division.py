#!/usr/bin/python3
def safe_print_division(a, b):
    try:
<<<<<<< HEAD
        res = a / b
    except ZeroDivisionError:
        res = None
    finally:
        print("Inside result: {:f}".format(res))

a = 5
b = 0
result = safe_print_division(a, b)
=======
        quotient = a / b
    except Exception as e:
        quotient = None
    finally:
        print("Inside result: {}".format(quotient))
    return quotient
>>>>>>> 9e2523d3bfcca18e21bf8648ddcd3c5ed819a993
