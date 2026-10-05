todos = []
askwhat = """What do you want to do?
    1. add a todo
    2. remove a todo
    3 list todos 
    4. complete a todo"""

def addTodo():
        task = input("What do i need to do?")
        todos.append(task)

def completeTodo():
    pass
def removeTodo():
    pass

def listTodos():
    print(todos)

def main():
    action = input(askwhat)
    if action == "1":
       addTodo()
       listTodos()



main()



