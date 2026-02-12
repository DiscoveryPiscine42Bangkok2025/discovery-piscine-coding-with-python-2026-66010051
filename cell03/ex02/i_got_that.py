#!/usr/bin/env python
s = input("What you gotta say? : ")
i=0

while i >= 0:
    if s != "STOP":
        s = input("I got that! Anything else? : ")
        i+=1
    else:
        break
