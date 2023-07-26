import random
from getch import getch
import os
import copy
fMap = {}

bCount = 0

treeDB = []

time = 0

dnc = "day"

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

#bear
bX = 5
bY = 1
fMap[bY][bX] = 'b'

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


# add item to inventory
def addItem(type):
    global notifCode
    inv.append(type)
    notifCode = True


#calculates the day night cycle
def calctime(t=False):
    global dnc, time, contrDisplay, contrDisplayNotif
    if t == True:
        time = time + 1
    if time > 60:
        time = 0
    if time > 45:
        dnc = 'night'
    else:
        dnc = 'day'
        
    contrDisplay = f"Player cords: X:{pX} Y:{pY}, Open Inventory: I, Time is {time}/60 ({dnc})"
    contrDisplayNotif = f"Player cords: X:{pX} Y:{pY}, Open Inventory: I, Time is {time}/60 ({dnc}) I You picked up an item! enter inv to remove notification."

#bear direction to player calc
def bDir():
    global bX, bY, bInp

    diffY = pY - bY
    diffX = pX - bX

    if abs(diffY) > abs(diffX):
        if diffY > 0:
            bInp = 's'
        else:
            bInp = 'w'
    else:
        if diffX > 0:
            bInp = 'd'
        else:
            bInp = 'a'


        
        

contrDisplay = f"Player cords: X:{pX} Y:{pY}, Open Inventory: I, Time is {time}/60 ({dnc})"
contrDisplayNotif = f"Player cords: X:{pX} Y:{pY}, Open Inventory: I, Time is {time}/60 ({dnc}) I You picked up an item! enter inv to remove notification."


#gameplay loop

while True:

#print
    os.system('clear')
 
    for item in fMap:
        if dnc == 'day':
            print(fMap[item])
            
    if notifCode == True:
        print(contrDisplayNotif)
    else:
        print(contrDisplay)
    
    uInp = getch()

#time
    calctime(t=True)

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
    
#other controls

    if uInp == 'i':
        while True:
            os.system('clear')
            print(f"{inv} press q to leave inv")
            invInp = getch()
            
            if invInp == 'q':
                notifCode = False
                break

#bear mode

    if random.randint(1,2) == 2:
        bDir()
    else:
        bInp = ''
    
    if bInp == 'w':
        if  bY-1 != 0 and fMap[bY-1][bX] == '_':
            fMap[bY][bX] = '_'
            bY = bY - 1
            fMap[bY][bX] = 'b'



    if bInp == 's':
        if  bY != 25 and fMap[bY+1][bX] == '_':
            fMap[bY][bX] = '_'
            bY = bY + 1
            fMap[bY][bX] = 'b'


    if bInp == 'd':
        if bX != 24 and fMap[bY][bX+1] == '_':
            fMap[bY][bX] = '_'
            bX = bX + 1
            fMap[bY][bX] = 'b'


    if bInp == 'a':
        if bX != 0 and fMap[bY][bX-1] == '_':
            fMap[bY][bX] = '_'
            bX = bX - 1
            fMap[bY][bX] = 'b'
    