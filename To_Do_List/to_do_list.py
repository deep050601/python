import os

if not "To_do_list" in os.listdir():
    os.mkdir("To_do_list")

def open_file(name):
    with open(f"To_do_list/{name}.txt", "r", encoding="utf-8") as f:
        print("\nYour Tasks:")
        print(f.read())

def new_file(name):
    a = int(input("If you want to enter a Task enter '1' and '0' for quit : "))
    if a == 1:
        with open(f"To_do_list/{name}.txt", "a+", encoding="utf-8") as f:
            while True:
                task = input("Enter a Task  : ")

                f.write(f"{task}\n")

                b = int(input("For continue enter '1' and '0' for quit : "))
                if b == 1:
                    continue
                else:
                    f.seek(0)
                    print("\nYour Tasks:")
                    print(f.read())
                    break
    else:
        print("You Quit ")

def delete_task(name):
    open_file(name)
    lin = int(input("enter line from you want to delete a task : "))
    try:
        with open(f"To_do_list/{name}.txt", "r", encoding="utf-8") as f:
            tasks = f.readlines()
        with open(f"To_do_list/{name}.txt", "w", encoding="utf-8") as f:
            for i, task in enumerate(tasks):
                if i != lin - 1:
                    f.write(task)
    except:
        print("Somthing went wrong!!")
    finally:
        open_file(name)

def marks_as_done(name):
    open_file(name)
    lin = int(input("Enter Task line you want to marks as complete : "))
    try:
        with open(f"To_do_list/{name}.txt", "r", encoding="utf-8") as f:
            tasks = f.readlines()
        with open(f"To_do_list/{name}.txt", "w", encoding="utf-8") as f:
            for i, task in enumerate(tasks):
                if i == lin - 1:
                    f.write(f"{task.strip()}  =  ✔️ complete\n")
                #   return
                else:
                    f.write(task)
    except Exception as e:
        print("Somthing went wrong!!", e)
    finally:
        open_file(name)

print("----------Welcome to To_Do_List App----------")
choise = int(
    input(
        "if you want to View Task Enter '1' \nfor create new file Enter '2' \nDelete Task from file Enter '3' \nFor tick Task as mark as done enter '4' : "
    )
)

if choise == 1:
    file = input(("Enter a file name for to view task : "))
    if f"{file}.txt" in os.listdir("To_do_list"):
        open_file(file)
    else:
        print("file not exist")
elif choise == 2:
    new_f = input(("Enter new file name : "))
    if not f"{new_f}.txt" in os.listdir("To_do_list"):
        with open(f"To_do_list/{new_f}.txt", "w") as f:
            new_file(new_f)
    else:
        print("file already exist ")
elif choise == 3:
    delete_f = input("Eenter file name from you want to Delete Task : ")
    if f"{delete_f}.txt" in os.listdir("To_do_list"):
        delete_task(delete_f)
    else:
        print("file not exist ")
elif choise == 4:
    done = input(("Enter a file name for to view task : "))
    if f"{done}.txt" in os.listdir("To_do_list"):
        marks_as_done(done)
    else:
        print("file not exist")
