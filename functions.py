def get_todos(filepath="todos.txt"):
    """ Read a text file and return the list of
    a to-do items.
    """
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """ Write the to-do items list in the text file.
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

# This is a way to run code below only while running this file not the main
# __name__ is the name of running file
if __name__ == "__main__":
    print("Hello from functions")