import argparse

""" A set of utils functions for strings exercises """

def _setArgs():
    """ Set menu arguments
    Return:
        parser instance
    """
    substrH = "substring to be checked"
    strH = "string to be compared against"

    parser = argparse.ArgumentParser()
    parser.add_argument("-T", type=str, required=True, help=substrH)
    parser.add_argument("-S", type=str, required=True, help=strH)
    return parser.parse_args()

def _setAnagramArgs():
    """ Set menu arguments for anagram exercises """
    pH = "non-empty string to be checked its anagrams"
    sH = "string to be compared against"

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", type=str, required=True, help=pH)
    parser.add_argument("-s", type=str, required=True, help=sH)
    return parser.parse_args()

def _getFrecFromStr(T):
    """
    Return:
        frec   (dict): frecuency dict of chars in T
        counter (int): counter of unique chars in T
    """
    frec = {key:0 for key in T}
    for key in frec:
        frec[key] += 1
    counter = len(frec)
    return frec, counter
