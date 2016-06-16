# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 17:35:30 2014

@author: alberto valente alberto@plumake.it
"""

import pyaudio
import wave
import sys
import serial
CHUNK = 1024

try:
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=0)
except Exception, e:
    print "Impossibile aprire la porta seriale: " + str(e)
    exit()

suoni = ("01_F.wav","04_C.wav","05_Db.wav","06_Bon.wav","07_Wha.wav","08_F.wav","09_Groove.wav","10_Synth.wav")

p = pyaudio.PyAudio()
while True:
    stringaDati = ser.read(9999)
    if(len(stringaDati)>0):
        print stringaDati
        try:
            i = int(stringaDati[0])
            wf = wave.open(suoni[i], 'rb')
            print suoni[i]
            stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                            channels=wf.getnchannels(),
                            rate=wf.getframerate(),
                            output=True)
            
            data = wf.readframes(CHUNK)
            
            while data != '':
                stream.write(data)
                data = wf.readframes(CHUNK)
            
            stream.stop_stream()
            stream.close()
            ser.flushInput()
        except Exception, e:
            print "boo: " + str(e)

p.terminate()
