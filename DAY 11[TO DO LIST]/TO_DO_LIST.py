# To-Do List (Console)
# Use: list, append/removeTo-Do List (Console)
to_do =[] # To-Do List (Console)
# Use: list, append/removeTo-Do List (Console)
to_do =[]
def manage_tasks():
    wants = input("add/remove/exit:").lower().strip()
    if wants =="add":
        new_task = input("what task you want to add:").lower().strip()
        to_do.append(new_task)
        print("new tasks list:",to_do)
    elif wants== "remove":
        remove_task = input("what task you want to remove:").lower().strip()
        if remove_task in to_do:
            to_do.remove(remove_task)
            print("new tasks list:",to_do)
        else:
            print("no task found in ")   
    elif wants=="exit":
        print("tasks list:",to_do)
        return False
    else:
        print("invalid input")        
       
while True :
    if manage_tasks() is False :
        break
    





