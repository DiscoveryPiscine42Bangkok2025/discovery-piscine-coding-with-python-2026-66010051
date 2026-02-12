#!/usr/bin/env python
import sys

args = sys.argv[1:]
arg_count = len(args)

if arg_count == 0:
    print("none")
else:
    print(f"parameters: {arg_count}")
    for arg in args:
        print(f"{arg}: {len(arg)}")