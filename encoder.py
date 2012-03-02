#! /usr/bin/env python

import clint
from clint.textui import puts, indent

morse_code_dict = {
    "A": "1 111",
    "B": "111 1 1 1",
    "C": "111 1 111 1",
    "D": "111 1 1",
    "E": "1",
    "F": "1 1 111 1",
    "G": "111 111 1",
    "H": "1 1 1 1",
    "I": "1 1",
    "J": "1 111 111 111",
    "K": "111 1 111",
    "L": "1 111 1 1",
    "M": "111 111",
    "N": "111 1",
    "O": "111 111 111",
    "P": "1 111 111 1",
    "Q": "111 111 1 111",
    "R": "1 111 1",
    "S": "1 1 1",
    "T": "111",
    "U": "1 1 111",
    "V": "1 1 1 111",
    "W": "1 111 111",
    "X": "111 1 1 111",
    "Y": "111 1 111 111",
    "Z": "111 111 1 1",

    "1": "1 111 111 111 111",
    "2": "1 1 111 111 111",
    "3": "1 1 1 111 111",
    "4": "1 1 1 1 111",
    "5": "1 1 1 1 1",
    "6": "111 1 1 1 1",
    "7": "111 111 1 1 1",
    "8": "111 111 111 1 1",
    "9": "111 111 111 111 1",
    "0": "111 111 111 111 111",
}


clint_args = clint.args.get(0)
clint_piped = clint.piped_in()


def encode(data):
    output = ""
    for letter in data.strip():
        if letter == " ":
            output += "    "
        else:
            output += morse_code_dict.get(letter.upper())
            output += "   "
    print output.strip()

if clint_args:
    encode(clint_args)
elif clint_piped:
    encode(clint_piped)
else:
    help = """
    Encode an ASCII string into a morse code string.

    Examples:
        ./encoder.py Hi
            ASCII string as first argument.

        ./encoder.py "Hello World"
            Use quotes to encode more than one word.

        echo "Hi" | ./encoder.py
            ASCII string can be piped in.

        python encoder.py Hi
    """
    puts(help)
