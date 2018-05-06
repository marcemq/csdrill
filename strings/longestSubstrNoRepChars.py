# Problem: longest substring without repeating characters
# taken from:
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# Examples:
# Input: "abcabcbb", Output: 3
# Input: "bbbbb", Output: 1
# Input: "pwwkew", Output: 3

import sys
from utils import _setOneStrInputArg

def getLengthOfLongestSubstr(s):
    seen = {}
    start, end, length = 0, 0, 0
    ans = ""

    while end < len(s):
        currentKey = s[end]
        if currentKey in seen and seen[currentKey] >= start:
            start = seen[currentKey] + 1
        else:
            seen[currentKey] = end
            end += 1
        if end - start > length:
            length = end - start
            ans = s[start:end]
    return length, ans

if __name__ == "__main__":
    args = _setOneStrInputArg()
    lengthOfLongestSubstr, substr = getLengthOfLongestSubstr(args.s)
    print("{}:{}".format(substr,lengthOfLongestSubstr))
