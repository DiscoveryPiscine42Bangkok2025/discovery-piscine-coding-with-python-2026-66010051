#!/usr/bin/env python
n_str = input("Give me a number: ")
n_float = float(n_str)

if n_float.is_integer():
    print("This number is an integer.")
else:
    print("This number is an decimal.")
