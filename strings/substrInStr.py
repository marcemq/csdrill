# Check if a substring characters are contained in a string
# Example
# INPUT: substr = ABCa, string = BDAECAa
# OUTPUT: ABCa IN BDAECAa

import sys
import argparse

def _setArgs():
    substrH = "substring to be checked"
    strH = "string to be compared against"

    parser = argparse.ArgumentParser(prog='tool',
        formatter_class=lambda prog:argparse.HelpFormatter(prog,max_help_position=30))
    parser.add_argument("--substr", "-s", type=str, required=True, help=substrH)
    parser.add_argument("--str", "-S", type=str, required=True, help=strH)
    return parser.parse_args()

def checkSubstrInStr(substr, str):
    frec = {key:0 for key in substr}
    for key in substr:
        frec[key] += 1
    counter = len(frec)

    for si in str:
        if si in frec:
            frec[si] -= 1
            if frec[si] == 0:
                counter -= 1
    if counter == 0:
        print("{} IN {}".format(substr, str))
    else:
        print("{} NOT IN {}".format(substr, str))

if __name__ == "__main__":
    args = _setArgs()
    checkSubstrInStr(args.substr, args.str)
