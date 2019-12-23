from bitstring import BitStream, BitArray
from midiutil.MidiFile import MIDIFile

mf = MIDIFile()
track = 0
time = 0
mf.addTempo(track, time, 240)

channel = 0

with open("me.png", "rb") as f:
    byte = f.read()

a = BitArray(byte)
line = a.bin
chunks = [line[i:i+9] for i in range(0, len(line), 9)]
decs = []

for chunk in chunks:
    c = list(chunk)
    value=0
    for i in range(len(c)):
	    digit = c.pop()
	    if digit == '1':
    		value = value + pow(2, i)
    decs.append(value)

notes = [50,52,53,55,57,59,60,62,64,65,67,69,71,72,74,76]
volume = [100,99,98,97,96,95,94,93,92,91,90,89,88,87,86,85,84,83,82,81,80,79,78,77,76,75,74,73,72,71,70,69]
bitone = []
bittwo = []

for letter in decs:
    bitone.append(notes[letter%16])
    bittwo.append(volume[int(letter/16)])

for (x,y) in zip(bitone,bittwo):
    duration = 1
    mf.addNote(track, channel, x, time, duration, y)
    time+=1

print("Working...")

with open("output.mid", 'wb') as outf:
    mf.writeFile(outf)
    print("Done!",end = '')
