#!/usr/bin/env python
import sys

if len(sys.argv) != 3:
    print("none")
else:
    start = int(sys.argv[1])
    stop = int(sys.argv[2])
    num = [i for i in range(start,stop+1)]
    print(num)