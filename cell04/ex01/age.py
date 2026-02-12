#!/usr/bin/env python
age_str = input("please tell me your age: ")
age_int = int(age_str)
print(f"you are currently {age_int} years old")

for i in range(10,31,10):
    print(f"In {i} years, you'll be {age_int + i} years old.")