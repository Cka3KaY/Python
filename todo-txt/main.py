todos = []
askwhat = """What do you want to do?
    1. add a todo
    2. remove a todo
    3. list todos 
    4. complete a todo

Answer>"""

def addTodo():
    task = input("What do you need to do?: ")
    todos.append(task)
    f = open("todos.txt", "a")
    f.writelines(f"{task}\n")
    print(f"added task {task}")

    

def completeTodo():
    target = input("What do you want to Complete?")
    f = open("todos.txt", "r")
    lines = f.readlines()
    kept = []
    for line in lines:
        if line.strip() != target.strip():
            kept.append(line)
    f = open("todos.txt", "w")
    f.writelines(kept)

def removeTodo(): 
    target = input("What do you want to remove?")
    f = open("todos.txt", "r")
    lines = f.readlines()
    kept = []
    for line in lines:
        if line.strip() != target.strip():
            kept.append(line)
    f = open("todos.txt", "w")
    f.writelines(kept)


 
def listTodos(): 
    f = open("todos.txt", "r")
    f = f.read()
    print(f)

def main():
    action = input(askwhat)
    if action == "1":
       addTodo()
       listTodos()
    if action == "3":
       listTodos()
    if action == "2":
       removeTodo()



main()



