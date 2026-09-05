import json

#read data from file
def read_file():
    try:
        with open("task_file.json","r") as f:
            my_task= json.load(f)
    except(FileNotFoundError, json.JSONDecodeError):
        my_task=[]

    return my_task


#1. function for add new task
def add_task():
    my_task= read_file()
        
    task = input("add your task: ")
    my_task.append(task)

    with open("task_file.json","w") as f:
        json.dump(my_task, f)

    print("your task added successfully\n")


#2. delete task
def dlt_task():
    my_task= read_file()
    num = int(input("which one task do you want to delete: "))

    if num > len(my_task):
        print("please enter valid number")
    else:
        print(num)
        print(my_task[num-1]," deleted")
        my_task.remove(my_task[num-1])

        with open("task_file.json","w") as f:
            json.dump(my_task,f)


#3. edit task
def edit_task():
    my_task= read_file()
    num = int(input("which one task do you want do edit: "))

    if num > len(my_task):
        print("task does not exist")
    else:
        my_task[num-1]= input("here you can edit: ")

        with open("task_file.json","w") as f:
            json.dump(my_task,f)


#4. show all task
def view_task():
    my_task = read_file()

    if len(my_task)==0:
        print("no task are added")
    else:
        print("your privious task are: ")
        for i, p_task in enumerate(my_task):
            print(i+1, p_task)

while True:
    print("\nTo_Do List ")
    print("1. do you want to add some task")
    print("2. do you want to delete some task")
    print("3. do you want to edit some tast")
    print("4. view")
    print("5. exit")

    choice = input("\nenter your choice: ")
    
    if(choice == "1"):
        add_task()

    elif(choice == "2"):
            dlt_task()
    
    elif(choice == "3"):
            edit_task()

    elif(choice =="4"):
        view_task()
    
    elif(choice == "5"):
        print("program ended")
        break

    else:
        print("invalid input")