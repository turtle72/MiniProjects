import random
from getch import getch
import os
fMap = {}



#base map no trees, movment etc
for item in range(1,26):
    fMap[item] = []
    for itemx in range(1,26):
        fMap[item].append('_')

#water left side
for item in fMap:
    for itemx in range(0,random.randint(2,4)):
        fMap[item][itemx] = 'w'
#water right side
    for itemy in range(random.randint(22,24),25):
        fMap[item][itemy] = 'w'

#player
pX = 12
pY = 13
fMap[pY][pX] = '@'



#trees
treeCount = 0
for item in fMap:
    while True:
        if item % 2 != 0:
            break
        treeLocal = random.randint(0,24)
        if fMap[item][treeLocal] == '_':
            fMap[item][treeLocal] = 't'
            treeCount = treeCount + 1
        if treeCount == 2:
            treeCount = 0
            break


while True:
    os.system('clear')
    
    for item in fMap:
        print(fMap[item])
    print(pY,pX)
    
    uInp = getch()
    
    if uInp == 'w':
        if  pY != 1 and fMap[pY-1][pX] == '_':
            fMap[pY][pX] = '_'
            pY = pY - 1
            fMap[pY][pX] = '@'

    if uInp == 's':
        if  pY != 25 and fMap[pY+1][pX] == '_':
            fMap[pY][pX] = '_'
            pY = pY + 1
            fMap[pY][pX] = '@'

    if uInp == 'd':
        if pX != 24 and fMap[pY][pX+1] == '_':
            fMap[pY][pX] = '_'
            pX = pX + 1
            fMap[pY][pX] = '@'

    if uInp == 'a':
        if pX != 0 and fMap[pY][pX-1] == '_':
            fMap[pY][pX] = '_'
            pX = pX - 1
            fMap[pY][pX] = '@'