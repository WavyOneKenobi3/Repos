# title of project (To-Do list)

#array for the the to-do list 
To_Do_List = {}
print("To-Do List\n")
print("Welcome to Your To-Do list app. ")
print("Select an option")


 
 #Add item to list (in array)
def add_list():
    task = input("Add Task\n ")
    Date_Task = input("Add Date\n ")
    To_Do_List.append({"Task": task, "Date": Date_Task})    
    
 #delete item off list (in array)
def delete_list():
    task = input("Delete Task: ")
    Date_Task = input("Delete Date: ")
    item_to_remove = {"Task": task, "Date": Date_Task}
    try: 
        if item_to_remove in To_Do_List:
        To_Do_List.remove(item_to_remove)
        print("Task removed.")
    else:
        print("Task not found in the list.")
    except: KeyError:
        print("Not in list")
        pass
    
 #Display list
def display_list():
    print(To_Do_List)


def play():  
    while True:
        try:
            user_input = input("1. Add Task \n2. Delete Task\n3. Show List\n4. Quit\n").strip() 
            if user_input == "1":
                add_list()
            elif user_input == "2":
                delete_list()
            elif user_input == "3":
                display_list()
            elif user_input == "4":
                print("Ending Program")
                break
            else:
                print("Invalid option. Please try again.")
        except: 
            print("ERROR")
            



play()


