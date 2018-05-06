# Problem: substring with concatenation of all words
# Taken from:
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
# Example
# Input: s = "barfoothefoobarman", words = ["foo","bar"]
# Output: [0,9]
#
# Explanation:
# Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
# The output order does not matter, returning [9,0] is fine too.
import sys
from utils import _getFrecFromStr, _setConcatAllWordsArgs, _concatListStrs

def finSubstrConcatIndex(s, words):
    p = _concatListStrs(words)
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
            if (end - start) == pSize:
                index.append(start)
            startKey = s[start]
            if startKey in frec:
                frec[startKey] += 1
                if frec[startKey] > 0: counter += 1
            start += 1
    return index

if __name__ == "__main__":
    args = _setConcatAllWordsArgs()
    index = finSubstrConcatIndex(args.s, args.w)
    print(index)
