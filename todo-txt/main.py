todos = []
askwhat = """What do you want to do?
    1. add a todo
    2. remove a todo
    3 list todos 
    4. complete a todo

Answer>"""

def addTodo():
    task = input("What do you need to do?: ")
    todos.append(task)
    f = open("todos.txt", "a")
    f.writelines(f"{task}, ")

    

def completeTodo():
    pass
def removeTodo():
    target = input("What do you want to remove?")
    f = open("todos.txt", "r")
    lines = f.read()
    kept = []
    for line in lines:
        if lines != target:
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



main()



