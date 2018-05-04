# Check if a substring characters are contained in another string
# Example
# INPUT: T = ABCa, S = BDAECAa
# OUTPUT: ABCa IN BDAECAa

import sys
from utils import _setArgs

def checkSubstrInStr(substr, mystr):
    frec = {key:0 for key in substr}
    for key in substr:
        frec[key] += 1
    counter = len(frec)

    for si in mystr:
        if si in frec:
            frec[si] -= 1
            if frec[si] == 0:
                counter -= 1
    if counter == 0:
        print("{} IN {}".format(substr, mystr))
    else:
        print("{} NOT IN {}".format(substr, mystr))

if __name__ == "__main__":
    args = _setArgs()
    checkSubstrInStr(args.T, args.S)
