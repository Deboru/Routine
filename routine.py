# TODO: Get start and end time

print('Good morning Debby, when did you wake up today?')
starttime = input()
print('And when do you plan to sleep?')
sleeptime = input()

routine = []
textFile = open('C:\\Users\\debby\\Desktop\\routine\\Routine.txt', 'w')

# TODO: Prompt user for the routine to do at each hour
for i in range(int(starttime), int(sleeptime)):
    print('What do you plan to do from %d:00 to %d:00? : ' %(i, i+1))
    routine.append(input())

# TODO: Create new txt file with routine formatted on C:\Users\debby\Desktop\Routine
print('Here is your schedule for today:')
for i in range(int(starttime), int(sleeptime)):
    print('%d:00 to %d:00 - %s' %(i, i+1, routine[i-int(starttime)]))
    textFile.write('%d:00 to %d:00 - %s\n' %(i, i+1, routine[i-int(starttime)]))


textFile.close()
