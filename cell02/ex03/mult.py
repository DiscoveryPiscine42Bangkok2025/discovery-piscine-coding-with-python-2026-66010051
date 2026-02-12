#!/usr/bin/env python
print("Enter the first number: ")
n1 = int(input())
print("Enter the second number:")
n2 = int(input())
mult = n1*n2
print(f"{n1} x {n2} = {mult}")

if mult == 0:
    print("The result is both positive and negative")
elif mult > 0:
    print("The result is positive")
else: 
    print("The result is negative")
    