# TODO: Get start and end time

print('Good morning Debby, when did you wake up today?')
starttime = input()
print('And when do you plan to sleep?')
sleeptime = input()

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
    textFile = open('C:\\Users\\debby\\Desktop\\routine\\Routine.txt', 'w')
    textFile.write('%d:00 to %d:00 - %s\n' %(i, i+1, routine[i-int(starttime)]))
    textFile.close()
