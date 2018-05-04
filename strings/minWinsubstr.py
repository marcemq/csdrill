# Problem taken from:
# https://leetcode.com/problems/minimum-window-substring/description/
# Example:
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"

import sys
from utils import _setArgs, _getFrecFromStr

def getMinWindow(S, T):
    frec, counter = _getFrecFromStr(T)
    start, end, length = 0, 0, sys.maxsize
    ans = ""
    while end < len(S):
        endKey = S[end]
        if endKey in frec:
            frec[endKey] -= 1
            if frec[endKey] == 0: counter -= 1
        end += 1
        while counter == 0:
            if end-start < length:
                length = end-start
                ans = S[start:end+1]
            startKey = S[start]
            if startKey in frec:
                frec[startKey] +=1
                if frec[startKey] > 0: counter += 1
            start += 1
    return ans

if __name__ == "__main__":
    args = _setArgs()
    minWindow = getMinWindow(args.S, args.T)
    print(minWindow)
