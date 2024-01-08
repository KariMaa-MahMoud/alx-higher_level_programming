#!/usr/bin/python3
matrix_mul = __import__('tests/100-matrix_mul.txt').matrix_mul

print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
