import easygui
from tkinter import Tk
from tkinter.filedialog import askdirectory

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing

# TODO: Get start and end time

print('Good morning Debby')
while True:
    print('When did you wake up today?')
    starttime = input()
    print('And when do you plan to sleep?')
    sleeptime = input()
    if (starttime.isdigit() and sleeptime.isdigit()):
        break
    else:
        print('I\'m sorry, I\'m going to need you to input numbers\n')

routine = []

# TODO: Prompt user for the routine to do at each hour
for i in range(int(starttime), int(sleeptime)):
    print('What do you plan to do from %d:00 to %d:00? : ' %(i, i+1))
    routine.append(input())

# TODO: Create new txt file with routine formatted on C:\Users\debby\Desktop\Routine
while True:
    print('Here is your schedule for today:')
    for i in range(int(starttime), int(sleeptime)):
        print('%d:00 to %d:00 - %s' %(i, i+1, routine[i-int(starttime)]))

    print('Do you want to make any changes?')
    yesno = input()
    if (yesno.lower() == "y") or (yesno.lower() == "yes"):
        print('What hour do you wish to change?')
        changehour = int(input())
        print('What do you plan to do from %d:00 to %d:00? : ' %(changehour, changehour+1))
        routine[changehour - int(starttime)] = input()
    else:
        break

print('Do you want to export to a text file?')
exportyesno = input()
if exportyesno.lower() == 'y' or 'yes':
    print('Where do you want to save it to?')
    path = askdirectory() # show an "Open" dialog box and return the path to the selected file
    #path = easygui.diropenbox()
    print('What do you want to name it?')
    name = input()
    textFile = open(path+'\\'+name +'.txt', 'w')
    for i in range(int(starttime), int(sleeptime)):
        textFile.write('%d:00 to %d:00 - %s\n' %(i, i+1, routine[i-int(starttime)]))
    print('The file ' + name+ '.txt has been saved in the directory ' + path)
    textFile.close()
