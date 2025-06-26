#!/usr/bin/env python3
import sys
import re

if len(sys.argv) == 2:
    print("none")
else:
    for word in sys.argv[1:]:
        if not re.search("ism", word):
            print(word + "ism")
