from bitstring import BitStream, BitArray
from mido import MidiFile
import base64

def bitstring_to_bytes(s):
    return bytes(int(s[i : i + 8], 2) for i in range(0, len(s), 8))

mid = MidiFile('output.mid')
i = 0
bitone = []
bittwo = []
notes = [50,52,53,55,57,59,60,62,64,65,67,69,71,72,74,76]
volume = [100,99,98,97,96,95,94,93,92,91,90,89,88,87,86,85,84,83,82,81,80,79,78,77,76,75,74,73,72,71,70,69]

print("working...")
for msg in mid.play():
    if(i%2==0):
        bitone.append(notes.index(msg.note))
        bittwo.append(volume.index(msg.velocity))
    i+=1

asciivalues=[]
for (x,y) in zip(bitone,bittwo):
    asciivalues.append((x)+(y*16))

strr=""
fin = []
first = True
for i,a in enumerate(asciivalues):
    fin.append(format(a, '09b'))

for a in fin:
    strr=strr+a

writestr=bitstring_to_bytes(strr)

with open('some_image.png', 'wb') as f:
    f.write(writestr)
