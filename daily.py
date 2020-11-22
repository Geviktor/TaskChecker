from os import system

system('clear')

#read username, xp and level elements
def readData():
    #grab the file and parse the elements
    filename = open('db', 'r')
    data = filename.readlines()
    data = data[0].split('|')

    #assign elements to variables
    user = data[0]
    xp = data[1]
    level = data[2].replace('\n','')
    
    filename.close()

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
    
    #take date and check date. only be DD/MM/YY format
    while True:
        date = input('What date do you want to do the task? [DD/MM/YYYY]: ')
        
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
    
    #open file in write mode, replace lines with the ones we edited
    a_file = open('db', 'w')
    a_file.writelines(list_of_lines)
    a_file.close()


