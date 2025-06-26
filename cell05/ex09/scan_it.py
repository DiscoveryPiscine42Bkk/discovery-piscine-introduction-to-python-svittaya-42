#!/usr/bin/env python3
import sys
import re

if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    text = sys.argv[2]
    # Match full words only using \b and escape special characters
    matches = re.findall(rf'\b{re.escape(keyword)}\b', text)
    if matches:
        print(len(matches))
    else:
        print("none")
