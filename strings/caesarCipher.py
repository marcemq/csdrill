# Problem : Caesar Cipher
# taken from: https://www.hackerrank.com/challenges/caesar-cipher-1/problem
#
# Example:
# Input: 11 middle-Outz 2 Output: okffng-Qwvb

import sys
import string
import re

def rotate(strg, k):
    k = k % len(strg)
    return strg[k:] + strg[:k]

def caesarCipher(s, k):
    alphabet = string.ascii_lowercase
    rotAlphabet = rotate(alphabet, k)
    encrypDict, encrypStr = {}, ""
    _notStr = re.compile('[a-zA-Z]+')
    for index, key in enumerate(alphabet):
        encrypDict[key] = rotAlphabet[index]
        
    for si in s:
        if not bool(_notStr.search(si)):
            encrypStr += si
        else:
            if si.isupper():
                encrypStr += encrypDict[si.lower()].upper()
            else:
                encrypStr += encrypDict[si]
    return encrypStr

if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    k = int(input().strip())
    result = caesarCipher(s, k)
    print(result)
