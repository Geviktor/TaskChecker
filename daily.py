from os import system
from datetime import datetime

#read username, xp and level elements
def readUser():
    #grab the file and parse the elements
    filename = open('db', 'r')
    data = filename.readlines()
    data = data[0].split('|')

    #assign elements to variables
    user = data[0]
    xp = data[1]
    level = data[2].replace('\n','')
    
    filename.close()

    return user,xp,level

def dateChecker():
    #take date and check date. only be DD/MM/YY format
    while True:
        date = input('What date do you want? [DD/MM/YYYY]: ')
        
        #check "/" character
        if '/' not in date:
            input('Date should be written in DD/MM/YYYY format! [PRESS ENTER]')
            continue
        
        #parse day, month and year
        parse = date.split('/')
        
        #date must be number
        try:
            for i in range(3):
                int(parse[i])
        except:
            input('Date should be written in DD/MM/YYYY format! [PRESS ENTER]')
            continue

        #day and month must be 2 character and year must be 4 character
        if len(parse[0]) != 2 or len(parse[1]) != 2 or len(parse[2]) != 4:
            input('Date should be written in DD/MM/YYYY format! [PRESS ENTER]')
            continue
        else:
            break

    return date

#create new task
def newTask():
    #take task
    task = input('Define the task you want to do: ')
    
    #take importance and check importence. only be high, normal or low.
    while True:
        importance = input('How important is this task? [high,normal,low]: ')
        importance = importance.lower()
        if importance == 'high' or importance == 'normal' or importance == 'low':
            break
        else:
            input('This value can only be High, normal, or low! [PRESS ENTER]')
    
    date = dateChecker()

    #combine information
    data = f"{task}|{importance}|{date}\n"
    
    #open file and append new line
    filename = open('db','a')
    filename.write(data)
    filename.close()

#edit a specific line
def editLine(linenumber,newdata):
    #open file in read mode, read lines change you want and assign their values to a variable
    a_file = open('db', 'r')
    list_of_lines = a_file.readlines()
    list_of_lines[linenumber] = f"{newdata}\n"
    a_file.close()

    #open file in write mode, replace lines with the ones we edited
    a_file = open('db', 'w')
    a_file.writelines(list_of_lines)
    a_file.close()

#Take tasks from file
def readTasks(date=f'{datetime.now().day}/{datetime.now().month}/{datetime.now().year}'):
    #open file
    filename = open('db','r')
    
    #take task as lists
    high = []
    normal = []
    low = []
    day = []

    
    for line in filename:
        line = line.split('|')
        line[2] = line[2].replace('\n','')
        
        #for dont take user line
        if "/" not in line[2]:
            continue
        
        #for take daily tasks
        if line[2] == date:
            day.append(line[0])

        #to receive tasks by level
        if line[1] == "high":
            high.append(line[0])
        elif line[1] == "normal":
            normal.append(line[0])
        else:
            low.append(line[0])

    return day,high,normal,low

#for print tasks to screen
def printTasks(day,high,normal,low):
    count = 1 #task counter
    whichtask = {} #to be able to choose tasks by numbers
    
    #print high level tasks
    print("HIGH LEVEL [30 XP]")
    for task in high:
        if task in day:
            print(f"{count}-"+task)
            whichtask[str(count)] = task
            count += 1
    print("\n")

    #print normal level tasks
    print("NORMAL LEVEL [15 XP]")
    for task in normal:
        if task in day:
            print(f"{count}-"+task)
            whichtask[str(count)] = task
            count += 1
    print("\n")

    #print low level tasks
    print("LOW LEVEL [7 XP]")
    for task in low:
        if task in day:
            print(f"{count}-"+task)
            whichtask[str(count)] = task
            count +=1
    print("\n")
    
    return whichtask

#to print the entire menu
def printMenu(date,day,high,normal,low):
    print('-'*120)
    welcome = f"Welcome {user}!     Your Level: {level}     Your XP: {xp}                 {date}"
    number = 60 - int(len(welcome)/2)
    print(" "*number + welcome + " "*number)

    whichtask = printTasks(day,high,normal,low)
    print('-'*120)
    print("")

    return whichtask


def completeTask(whichtask,what="delete"):
    try:
        tasknumber = input("Please give task number: ")
        if int(tasknumber) > len(whichtask) or int(tasknumber) < 1:
            input("No such task found! [PRES ENTER]")
        else:
            task = whichtask[tasknumber]

            #Take lines in file
            filename = open('db','r')
            lines = filename.readlines()

            #find task level
            for line in lines:
                if line.strip('\n').split('|')[0] == task:
                    tasklevel = line.strip('\n').split('|')[1]
            filename.close()
            
            if what == "complete":
                #edit user xp
                if tasklevel == "high":
                    lines[0] = f'{lines[0].split("|")[0]}|{str(int(lines[0].split("|")[1]) + 30)}|{lines[0].split("|")[2]}'
                elif tasklevel == "normal":
                    lines[0] = f'{lines[0].split("|")[0]}|{str(int(lines[0].split("|")[1]) + 15)}|{lines[0].split("|")[2]}'
                else:
                    lines[0] = f'{lines[0].split("|")[0]}|{str(int(lines[0].split("|")[1]) + 7)}|{lines[0].split("|")[2]}'

            print(lines)

            #write lines
            filename = open('db','w')
            
            for line in lines:
                if line.strip('\n').split('|')[0] != task:
                    filename.write(line)

            filename.close()

    except:
        input("Task number must be a number! [PRESS ENTER]")
        

def checkLevel():

    #take lines in file
    filename = open('db','r')
    lines = filename.readlines()
    filename.close()

    #find xp and level
    xp = int(lines[0].split("|")[1])
    level = int(lines[0].split("|")[2])

    #check xp and level
    if xp >= level * 1337:
        level += 1

    #edit user line
    lines[0] = f'{lines[0].split("|")[0]}|{str(xp)}|{str(level)}\n'

    #write lines
    filename = open('db','w')

    for line in lines:
        filename.write(line)

    filename.close()


date = f'{datetime.now().day}/{datetime.now().month}/{datetime.now().year}'
while True:
    checkLevel()
    user,xp,level = readUser()
    day,high,normal,low = readTasks(date)
    
    system('clear')
    whichtask = printMenu(date,day,high,normal,low)
    
    print("[1] Complete task")
    print("[2] Add new task")
    print("[3] Delete task")
    print("[4] See another day's task")
    print("[Q] Exit")
    print("")

    choice = input("What do you want to do?: ")
    choice = choice.lower()

    if choice == "1":
        completeTask(whichtask,"complete")
    elif choice == "2":
        newTask()
    elif choice == "3":
        completeTask(whichtask)
    elif choice == "4":
        date = dateChecker()
    elif choice == "q":
        break
    else:
        input("Your selection is not in the menu! [PRESS ENTER]")
