#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("none")
else:
    zs = ''.join([c for c in sys.argv[1] if c == 'z'])
    print(zs if zs else "none")
