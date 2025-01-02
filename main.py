# title of project (To-Do list)
print("To-Do List\n")

#array for the the to-do list 
Task = []
addTask = str()
addDate = float()
 
def toDoList():
    keep_Going = True
    
    while keep_Going:
        try:
            addTask = str(input(" Input Task "))      #user input
            addDate = float(input("date of Task "))     #date task is due
            Task.append(addTask)                        #append user input to array
            Task.append(addDate)
        except: 
            print("ERROR")
        else:    
            print(Task)         
        newVaules = input("Do you wnant to add another Task? Y or N ")
        if newVaules == "Y" or "y":
            continue
        elif newVaules == "N" or "n":
            break 
    
toDoList()
#delete item off list (in array)

