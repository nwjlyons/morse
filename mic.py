#!/usr/bin/python

import alsaaudio
import audioop


inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK)
inp.setchannels(1)
inp.setrate(8000)
inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
inp.setperiodsize(160)


listen = False
history = []
while True:
    l, data = inp.read()
    if l:
        volume = audioop.max(data, 2)

        if volume >= 19000:
            listen = True

        if listen:
            history.append(volume)

        if len(history) >= 15:
            if max(history) >= 25000:
                print "1"
            else:
                print " "
            listen = False
            history = []
