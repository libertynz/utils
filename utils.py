"""
Some useful utilities for python, such as current directory, etc.
"""


def make_snake_case(text: str) -> str:
    """
    A very basic way to converts some text into snake case.
    Strips out any non a-z, 0-9 characters.
    :param text:
    :return: a string which snake cases the text provided
    """
    chars = 'abcdefghijklmnopqrstuvwxyz1234567890_'
    unclean = text.lower().strip().replace(' ', '_')
    return ''.join(e for e in unclean if e in chars)


if __name__ == '__main__':
    print(make_snake_case(' Héllø Wörld   '))
