#! /usr/bin/env python

import clint

morse_code_dict = {
    "1 111": "A",
    "111 1 1 1": "B",
    "111 1 111 1": "C",
    "111 1 1": "D",
    "1": "E",
    "1 1 111 1": "F",
    "111 111 1": "G",
    "1 1 1 1": "H",
    "1 1": "I",
    "1 111 111 111": "J",
    "111 1 111": "K",
    "1 111 1 1": "L",
    "111 111": "M",
    "111 1": "N",
    "111 111 111": "O",
    "1 111 111 1": "P",
    "111 111 1 111": "Q",
    "1 111 1": "R",
    "1 1 1": "S",
    "111": "T",
    "1 1 111": "U",
    "1 1 1 111": "V",
    "1 111 111": "W",
    "111 1 1 111": "X",
    "111 1 111 111": "Y",
    "111 111 1 1": "Z",

    "1 111 111 111 111": "1",
    "1 1 111 111 111": "2",
    "1 1 1 111 111": "3",
    "1 1 1 1 111": "4",
    "1 1 1 1 1": "5",
    "111 1 1 1 1": "6",
    "111 111 1 1 1": "7",
    "111 111 111 1 1": "8",
    "111 111 111 111 1": "9",
    "111 111 111 111 111": "0",
}


def decode(data):
    words = data.rstrip('\n').split("       ")
    output = ""
    for word in words:
        letters = word.split("   ")
        for letter in letters:
            output += morse_code_dict.get(letter, " ")
        output += " "
    print output


clint_args = clint.args.get(0)
clint_piped = clint.piped_in()


if clint_args:
    decode(clint_args)
elif clint_piped:
    decode(clint_piped)
else:
    while True:
        f = open("my_pipe", "r")
        data = f.read()
        decode(data)
        f.close()
