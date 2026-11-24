from os import system, name, path

tasklist = []
user_option = ''

# checks if the file exists
if path.exists("tasklist.txt"):
    # reads the tasks file and appends the elements to the tasklist array
    with open("tasklist.txt", "r", encoding="utf-8") as file: 
        for line in file:
            tasklist.append(line.strip())
else:
    # create a new file if it doesnt exist
    with open("tasklist.txt", "w", encoding="utf-8") as file:
        pass 

# while the user doesnt choose to leave
while user_option != 'E':    
    # shows the tasklist
    for index, task in enumerate(tasklist):
        print(f"{index + 1} - {task}")
        
    print("\nOptions: \n")
    print("A]dd Task")
    print("C]heck Task as Done") 
    print("U]ncheck All Tasks")
    print("R]emove Task")
    print("E]xit \n")

    # gets user choice
    user_option = str(input("> ")).upper()

    match user_option:
        case 'A':
            task_to_add = str(input("Task to add: "))
            tasklist.append(task_to_add)
        case 'C':
            try:
                task_to_check_index = int(input("Number of the task to check: ")) - 1
                task_to_check = tasklist[task_to_check_index]

                if "( Check! )" in task_to_check:
                    print("Task already checked!")
                else:
                    tasklist[task_to_check_index] = task_to_check + " ( Check! )"                    

            except IndexError:
                print("Invalid task!")
            except ValueError:
                print("Invalid number!")

        case 'U':
            tasklist = [task.replace(" ( Check! )", "") for task in tasklist]

        case 'R':
            try:
                task_to_remove = int(input("Number of the task to remove: ")) - 1
                tasklist.pop(task_to_remove)
            except IndexError:
                print("Invalid task!")
            except ValueError:
                print("Invalid number!")

        case 'E':
            break

        case _:
            print("Invalid option!")

        # clear the terminal
    system('cls' if name == 'nt' else 'clear')

# save the tasklist in the file
with open("tasklist.txt", "w", encoding="utf-8") as file: 
    for task in tasklist:
        file.write(f"{task.strip()} \n")
