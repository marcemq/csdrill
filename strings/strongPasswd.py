# Problem: strong password
# taken from:
# https://www.hackerrank.com/challenges/strong-password/problem
#
# Example:
# Input: 3 Ab1 Output: 3

import sys
import re

MINLENTGTH = 6
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    minNum = 0
    _dg = re.compile('\d')
    _lc = re.compile('[a-z]+')
    _uc = re.compile('[A-Z]+')
    _sc = re.compile('[!@#$%^&*()\-+]+')
    containsDg = bool(_dg.search(password))
    containsLc = bool(_lc.search(password))
    containsUp = bool(_uc.search(password))
    containsSc = bool(_sc.search(password))
    if not containsDg: minNum += 1
    if not containsLc: minNum += 1
    if not containsUp: minNum += 1
    if not containsSc: minNum +=1
    return max(MINLENTGTH-n, minNum)

if __name__ == "__main__":
    n = int(input().strip())
    password = input().strip()
    answer = minimumNumber(n, password)
    print(answer)
