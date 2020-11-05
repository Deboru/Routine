import easygui
from tkinter import Tk
from tkinter.filedialog import askdirectory
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')
logging.disable(logging.DEBUG) #uncomment for final 

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing

# TODO: Get start and end time

print('Good morning Debby')
while True:
    print('When did you wake up today? (please enter 24 hr clock)')
    starttime = input()
    print('And when do you plan to sleep? (please enter 24 hr clock)')
    sleeptime = input()
    if (starttime.isdigit() and sleeptime.isdigit()):
        break
    else:
        print('I\'m sorry, I\'m going to need you to input numbers\n')

routine = []
steps = []
i = int(starttime)

# TODO: Prompt user for the routine to do at each hour
while i < int(sleeptime):
    print('What do you plan to do from %d:00? : ' %(i))
    routine.append(input())
    if i+1 != int(sleeptime):
        print('when will you finish? : ')
        steps.append(int(input())-i)
    else:
        steps.append(1)
    print('you plan to',routine[-1],'from %d:00 to %d:00' %(i,i+steps[-1]))
    i += steps[-1]
    logging.debug(i)

# TODO: Create new txt file with routine formatted on C:\Users\debby\Desktop\Routine
while True:
    print('Here is your schedule for today:')
    k = 0
    i = int(starttime)
    while i < int(sleeptime):
        print('%d:00 to %d:00 - %s' %(i, i+steps[k], routine[k]))
        i += steps[k]
        k += 1

    print('Do you want to make any changes?')
    yesno = str(input()).strip()
    if (yesno.lower() == "y") or (yesno.lower() == "yes"):
        print('What start hour activity do you wish to change?')
        changehour = int(input())
        #TODO: What to do when the change hour is not in our range
        print('What do you plan to do from %d:00 : ' %(changehour))

        #find the corresponding routine to change
        k = 0
        while k < len(routine):
            i = int(starttime)
            while i < int(sleeptime):
                if i == changehour:
                    break
                else:
                    i += steps[k]
                    k +=1
            break
        routine[k] = str(input())
        
    else:
        break

print('Do you want to export to a text file?')
exportyesno = str(input())
if (exportyesno.lower() == 'y') or (exportyesno.lower() == 'yes'):
    print('Where do you want to save it to?')
    path = askdirectory() # show an "Open" dialog box and return the path to the selected file
    #path = easygui.diropenbox()
    print('What do you want to name it?')
    name = input()
    textFile = open(path+'\\'+name +'.txt', 'w')

    k = 0
    i = int(starttime)
    while i < int(sleeptime):
        textFile.write('%d:00 to %d:00 - %s\n' %(i, i+steps[k], routine[k]))
        i += steps[k]
        k += 1
        
    print('The file ' + name+ '.txt has been saved in the directory ' + path)
    textFile.close()

else:
    print('Have a nice day!')
