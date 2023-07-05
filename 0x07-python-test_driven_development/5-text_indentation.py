#!/usr/bin/python3
"""Module built for Python 0x07 task 4. Error in project formatting scheme \
advances file numbering +1 for every task after 0.
"""


def text_indentation(text):
    """Function that prints text with 2 new lines after each of the \
    characters ".", ",", and '?' :

    Args:
        text (str): text to be edited

    """
    punctuation_marks = ['.', '?', ':']
    new_text = ""
    current_line = ""
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    for char in text:
        if char in punctuation_marks:
            new_text += current_line.strip() + f'{char}\n\n'
            current_line = ""
        else:
            current_line += char
    new_text += current_line.strip()
    print(new_text)
