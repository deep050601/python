import os

if not "expense_notes" in os.listdir():
   os.mkdir("expense_notes")

def total(name):
    Total_money = 0
    with open(f"expense_notes/{name}.txt", "r")as f:
      i = 0
      while True:
         i += 1
         line = f.readline()
         if not line:
               break
         ex = line.split(":")[1]
         Total_money = Total_money + int(ex)
      print(f"Total expense is {Total_money} Rupees ")

def open_file(name):
    with open(f"expense_notes/{name}.txt", "r") as f:
        print(f.read())
    total(name)

def new_file(name):
    a=int(input("If you want to enter an entary enter '1' and '0' for quit : " ))
    if a==1:
       
        while True:
            entry=input("Enter entry in this formet (task:spending) : ")
            f=open(f"expense_notes/{name}.txt","a")
            f.writelines(f"{entry}\n")
            f.close() 
            b=int(input("For continue enter '1' and '0' for quit : "))
            if b==1:
                continue
            else:
                with open(f"expense_notes/{name}.txt","r")as f:
                    print(f.read())
                # total(name)
                break
    else :
        print("You Quit ")

def delete_expense(name):
    open_file(name)
    lin=int(input("Enter a line you want to delete : "))
    try:
        with open (f"expense_notes/{name}.txt","r")as f:
            lines=f.readlines()

        with open (f"expense_notes/{name}.txt","w")as f:
            for index,line in enumerate(lines):
                if index!=lin-1:
                    f.write(line)
    except:
        print("Somthing went wrong!!")
    finally:
        open_file(name)

print("----------Welcome to Expense tracker----------")
choise=int(input("if you want to open file Enter '1' for create new file Enter '2' and Delete Expense from file Enter '3': "))

if choise==1:
   file=input(("Enter a file name for opening a file : "))
   if f"{file}.txt" in os.listdir("expense_notes"): 
      open_file(file)
   else:
       print("file not exist")
elif choise==2:
    new_f=input(("Enter new file name : "))
    if not f"{new_f}.txt" in os.listdir("expense_notes"):
      with open (f"expense_notes/{new_f}.txt","w") as f:
         new_file(new_f)
    else:
        print("file already exist ")
elif choise==3:
    delete_f=input("Eenter file name from you want to Delete Expense : ")
    delete_expense(delete_f)

