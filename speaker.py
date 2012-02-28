#! /usr/bin/env python

import time
import clint
import envoy


clint_args = clint.args.get(0)
clint_piped = clint.piped_in()


def sound_it(data):
    data = data.strip()
    for char in data:
        if char == "1":
            # print "\a1"
            print "1"
            envoy.run("play -v500 button-toggle-off.ogg")
            # time.sleep(.2)
        else:
            print " "
            envoy.run("play -v10 button-toggle-off.ogg")
            # time.sleep(.3)


if clint_args:
    sound_it(clint_args)
elif clint_piped:
    sound_it(clint_piped)
