import random

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
    
            

for item in fMap:
    print(fMap[item])