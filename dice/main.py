from getch import getch
import random
import os
import time
def dice(diced):
    
    dList = diced.lower().split("d")
    count = int(dList[0])
    num = int(dList[1])
    
    dOutput = 0
    
    for item in range(count):
        dOutput += random.randint(1,num)

    
    return(dOutput)

Uinp = '0'
baseDice = 0
while Uinp != 'E':

    os.system("clear")

    print(f""" 
          ____________________________
                    DND Dice
                    
             Last roll was  {baseDice}
            
              E:exit 1:enter roll
          ____________________________
          """)

    Uinp = getch().lower()
    

    
    if Uinp == 'E':
        break
    elif Uinp == '1':
        baseDice = dice(input("Enter your roll in the format of (amount of dice)d(dice sides) "))
        
    else:
        print("please enter E or 1")
        time.sleep(5)
