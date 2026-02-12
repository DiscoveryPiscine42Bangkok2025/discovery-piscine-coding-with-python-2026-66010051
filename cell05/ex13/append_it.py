#!/usr/bin/env python
import sys

match sys.argv:
    case [_]:
        print("none")
        
    case [_, *args]:
        for arg in args:
            match arg:
                case s if s.endswith("ism"):
                    continue
                case s:
                    print(f"{s}ism")