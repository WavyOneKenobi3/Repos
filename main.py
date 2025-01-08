# title of project (To-Do list)

#array for the the to-do list 
To_Do_List = {}

print("To-Do List\n")
print("Welcome to Your To-Do list app. ")

 
 #Add item to list (in array)
def add_list():
    task = input("Add Task\n ")
    Date_Task = input("Add Date\n ")
    To_Do_List.update({"Task": task, "Date": Date_Task})    
    
 #delete item off list (in array)
def delete_list():                                          
    task = input("Delete Task: ")
    if task in To_Do_List:                               
        del To_Do_List[task]
        print("Task removed.")
    else:
        print("Task not found in the list.")


def play():  
    while True:
        print("Select an option")
        user_input = input("1. Add Task \n2. Delete Task\n3. Show List\n4. Quit\n").strip() 
        if user_input == "1":
            add_list()
        elif user_input == "2":
            delete_list()
        elif user_input == "3":
            print(To_Do_List)
        elif user_input == "4":
            print("Ending Program")
            break
        else:
            print("Invalid option. Please try again.")
            




play()







  
