import streamlit as st
from functions import *
import os

FILE_PATH = r"todo.txt"

todos = get_todos(file_path=FILE_PATH)


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    print(todos)
    write_todo(FILE_PATH,todos)

st.title("""todo app""")


for index,todo in enumerate(todos):
    check_box = st.checkbox(todo, key=todo)
    if check_box:
        todos.pop(index)
        write_todo(FILE_PATH,todos)
        del st.session_state[todo]

add = st.text_input("enter todo", placeholder="Add new todo", on_change=add_todo, key="new_todo")


st.session_state

