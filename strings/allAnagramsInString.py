# Problem taken from:
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
# Example:
# Input: s: "cbaebabacd" p: "abc"
# Output: [0, 6]
#
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".

import sys
from utils import _getFrecFromStr, _setAnagramArgs

def findAnagramsIndex(s, p):
    frec, counter = _getFrecFromStr(p)
    start, end, pSize = 0, 0, len(p)
    index = []

    while end < len(s):
        endKey = s[end]
        if endKey in frec:
            frec[endKey] -= 1
            if frec[endKey] == 0: counter -=1
        end += 1
        while counter == 0:
            if end - start == pSize:
                index.append(start)
            startKey = s[start]
            if startKey in frec:
                frec[startKey] += 1
                if frec[startKey] > 0: counter += 1
            start += 1
    return index

if __name__ == "__main__":
    args = _setAnagramArgs()
    index = findAnagramsIndex(args.s, args.p)
    print(index)
