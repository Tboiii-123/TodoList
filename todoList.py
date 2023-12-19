#Creating a new task

tasks=[]
Removed_task=[]


def add_task(name,date):
    task = {"description":name,
            "status": "INCOMPLETE",
            "due_date": date
            }
    
    tasks.append(task)



def view_task():
    if  tasks==[]:
        print("No task added in the list")
    else:
        task_number=1
        for i in tasks:
            print(f"\n{task_number}.   {i['description']}               (Status:{i['status']} , Due_date:{i['due_date']})")
            
            task_number+=1
    
def mark_task(task_number):
    if  task_number <= len(tasks):
        task=tasks[task_number-1]
        task["status"]="COMPLETE"
        print(f"\nTask {task['description']} marked as completed")

    else:
        
        print("Your task_number hasn't reached the number")


def remove_task(task_number):
    if task_number<=len(tasks):
        removed_task=tasks.pop(task_number-1)
        Removed_task.append(removed_task)
        
        print(f"\nTask {removed_task['description']} has been removed form the content")

    else:
        print("\nYour task_number hasn't reached the number")

def removed_task():
    task_number=1
    for i in Removed_task:
            print(f"\n{task_number}.   {i['description']}               (Status:{i['status']} , Due_date:{i['due_date']})")
            
            task_number+=1
    

def Help():
    print("""

Choose your option\n
1 = To add a task\n
2 = To view thas task\n
3=  To mark task complete\n
4 =  To remove a task\n
5 = To view removed task\n
6 =To exit\n
help = For review of the details


""")



print("Choose your option\n")
print("1 = TO add a task\n")
print("2 = To view thas task\n")
print("3 = TO mark task complete\n")
print("4 = TO remove a task\n")
print("5= To view removed task\n")
print("6 =To exit\n")
print("help = For review of the details")


time=True
while time:


    choice =input("\nEnter  your choice:")


    if choice =='1':
        print("Adding Task.........\n")
        Task_name =input("Insert your Task name here:")
        date =input("Insert the date of fillup:")
        add_task(Task_name,date)
    elif choice =='2':
        print("Viewing Task\n")
        view_task()
    elif choice =='3':
        print("Marking task complete\n")
        try:
            task_number =int(input("Insert your task number to be marked completed:"))
            mark_task(task_number)
        except ValueError:
            print("\nInteger required not String")

    elif  choice =='4':
        print("Removing task\n")
        try:
            remove_Task=int(input("Insert your number to remove:"))
            remove_task(remove_Task)
        except ValueError:
            print("\nInteger required not String")

            

    elif choice == '5':
        print("Removed task view")
        removed_task()
    elif choice =='help':
        print("\nGetting help......\n")
        Help()
        
        
    elif choice =='6':
        
        print("Exiting to_do_list")
        time=False
    else:
        print("Invalid choice of Number entered")
    
    
    
