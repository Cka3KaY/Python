todos = []
askwhat = """What do you want to do?
    1. add a todo
    2. remove a todo
    3 list todos 
    4. complete a todo

    """

def addTodo():
    task = input("What do you need to do?: ")
    todos.append(task)
    f = open("todos.txt", "w")
    f.write(task)

    

def completeTodo():
    pass
def removeTodo():
    pass

def listTodos(): # FIX
    f = open("todos.txt", "r")
    f.read()
    print(f)

def main():
    action = input(askwhat)
    if action == "1":
       addTodo()
       listTodos()



main()



