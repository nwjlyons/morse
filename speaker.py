#! /usr/bin/env python

import clint
import envoy


clint_args = clint.args.get(0)
clint_piped = clint.piped_in()


def sound_it(data):
    data = data.strip()
    for char in data:
        if char == "1":
            print "1"
            envoy.run("play -v5 button-toggle-off.wav")
        else:
            print " "
            envoy.run("play -v1 button-toggle-off.wav")


if clint_args:
    sound_it(clint_args)
elif clint_piped:
    sound_it(clint_piped)
