#!/usr/bin/env python
i = 0

while i <= 10:
    print(f"Table de {i}:", end= " ")
    j=0
    while j <= 10:
        mult = i*j
        print(f"{mult}", end=" ")
        j+=1
    print("\n")
    i+=1
    