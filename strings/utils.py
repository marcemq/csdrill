import argparse

""" Utils to set menu arguments"""

def _setArgs():
    """ Set menu arguments for strings exercises.
    Return:
        parser instance
    """
    substrH = "substring to be checked"
    strH = "string to be compared against"

    parser = argparse.ArgumentParser(prog='tool',
        formatter_class=lambda prog:argparse.HelpFormatter(prog, max_help_position=30))
    parser.add_argument("--substr", "-s", type=str, required=True, help=substrH)
    parser.add_argument("--mystr", "-S", type=str, required=True, help=strH)
    return parser.parse_args()
