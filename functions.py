def get_todos(file_path):
    """     
    this function will return todos from todo.txt file.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        todos = file.readlines()
    return todos




def write_todo(file_path,todo):
    """
    this function will wrtie your todo to todo.txt.
    """
    with open (file_path, "w", encoding="utf-8") as file:
        file.writelines(todo)



#is only executed when the script is run directly, not when it's imported as a module.
if __name__ == "__main__":
    print(".................")