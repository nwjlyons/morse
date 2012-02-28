#!/usr/bin/python

import alsaaudio
import audioop
import clint
import signal
import sys


inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK)
inp.setchannels(1)
inp.setrate(8000)
inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
inp.setperiodsize(160)


listen = False
history = []
output = ""


def signal_handler(signal, frame):
    f = open("my_pipe", "w")
    f.write(output)
    f.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

while True:
    l, data = inp.read()
    if l:
        volume = audioop.max(data, 2)

        if "--debug" in clint.args:
            print volume

        if volume >= 1900:
            listen = True

        if listen:
            history.append(volume)

        if len(history) >= 15:
            if max(history) >= 9000:
                print "1"
                output += "1"
            else:
                print " "
                output += " "
            listen = False
            history = []
