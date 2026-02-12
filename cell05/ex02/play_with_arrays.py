#!/usr/bin/env python
numbers =  [2, 8, 9, 48, 8, 22, -12, 2]
print(f"Original array: {numbers}")

for i in range(len(numbers)):
    numbers[i] = numbers[i] + 2

print(f"New array: {numbers}")