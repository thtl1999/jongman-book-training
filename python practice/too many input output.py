# If there are too many input or output,
# cannot use input() and print()
# import sys to use faster IO functions

import sys

def input():
    return sys.stdin.readline()

def print(sth):
    sys.stdout.write(str(sth)+'\n')