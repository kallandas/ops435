#!/usr/bin/env python3
# Author: Ji Yong Hwang
# Author ID: jyhwang
# Date Created: 2022/09/20

import sys

if len(sys.argv) == 1:
    timer = 3
else:
    timer = int(sys.argv[1])

while timer != 0:
    print(timer)
    timer = timer - 1

print("blast off!")
