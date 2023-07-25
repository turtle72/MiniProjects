import random
from getch import getch
import os
fMap = {}

treeDB = []

inv = []

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
            treeTuple = (item,treeLocal)
            treeDB.append(treeTuple)
            treeCount = treeCount + 1
        if treeCount == 2:
            treeCount = 0
            break

notifCode = False

def addItem(type):
    global notifCode
    inv.append(type)
    notifCode = True
    
contrDisplay = f"Player cords: X:{pX} Y:{pY} Open Inventory: I"
contrDisplayNotif = f"Player cords: X:{pX} Y:{pY} Open Inventory: I You picked up an item! enter inv to remove notification."

while True:

#print
    os.system('clear')
 
    for item in fMap:
        print(fMap[item])
    if notifCode == True:
        print(contrDisplayNotif)
    else:
        print(contrDisplay)
    
    uInp = getch()

#movement
    if uInp == 'w':
        if  pY != 1 and fMap[pY-1][pX] == '_':
            fMap[pY][pX] = '_'
            pY = pY - 1
            fMap[pY][pX] = '@'
        elif pY != 1 and fMap[pY-1][pX] == 't':
            if random.randint(1,15) == 5:
                addItem("berry")


    if uInp == 's':
        if  pY != 25 and fMap[pY+1][pX] == '_':
            fMap[pY][pX] = '_'
            pY = pY + 1
            fMap[pY][pX] = '@'
        elif pY != 25 and fMap[pY+1][pX] == 't':
            if random.randint(1,15) == 5:
                addItem("berry")

    if uInp == 'd':
        if pX != 24 and fMap[pY][pX+1] == '_':
            fMap[pY][pX] = '_'
            pX = pX + 1
            fMap[pY][pX] = '@'
        elif pX != 24 and fMap[pY][pX+1] == 't':
            if random.randint(1,15) == 5:
                addItem("berry")

    if uInp == 'a':
        if pX != 0 and fMap[pY][pX-1] == '_':
            fMap[pY][pX] = '_'
            pX = pX - 1
            fMap[pY][pX] = '@'
        elif pX != 0 and fMap[pY][pX-1] == 't':
            if random.randint(1,15) == 5:
                addItem("berry")
    
#other controllers

    if uInp == 'i':
        while True:
            os.system('clear')
            print(f"{inv} press q to leave inv")
            invInp = getch()
            
            if invInp == 'q':
                notifCode = False
                break