#!/usr/bin/env python
import sys
import re

if len(sys.argv) != 2:
    print("none")
else:
    word = input("What was the parameter? ")
    param = sys.argv[1]

    matches = re.findall(param, word)
    
    if matches:
        print("Good Job!")
    else:
        print("Nope, sorry")
    