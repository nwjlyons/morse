#!/usr/bin/python

import alsaaudio
import audioop

inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK)

inp.setchannels(1)
inp.setrate(8000)
inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
inp.setperiodsize(160)

# listen = True
# count = 0
listen = False
history = []
while True:
    l, data = inp.read()
    if l:
        volume = audioop.max(data, 2)

        if volume >= 20000:
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


        # if listen:
        #     print "listening ", volume
        #     if volume >= 20000:
        #         print "1"
        #         listen = False
        #     elif volume >= 5000:
        #         print " "
        #         listen = False
        # else:
        #     print "not listening ", volume
        #     if count >= 15:
        #         listen = True
        #         count = 0
        #     else:
        #         count += 1
