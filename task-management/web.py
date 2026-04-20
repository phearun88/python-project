import streamlit as st
import function

todos = function.get_todos()

def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    function.write_todos(todos)


st.title('My Todo App')
st.subheader('This is your todo application.')
st.write("This app to increase your productivity.")

for index, todo in enumerate(todos):
   checkbok = st.checkbox(todo, key=todo)
   if checkbok:
       todos.pop(index)
       function.write_todos(todos)
       del st.session_state[todo]
       st.rerun()

st.text_input(label="", placeholder="Enter your todo...", on_change=add_todo, key='new_todo')
#st.session_state