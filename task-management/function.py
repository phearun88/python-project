FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Returns a list of todos from the file """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg,filepath=FILEPATH):
    """ Writes todos to the file """
    with open(filepath, "w") as file:
         file.writelines(todos_arg)