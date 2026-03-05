import streamlit as st
import function

todos = function.get_todos()

st.title('Todos')
st.subheader('This is your todo application.')
st.write("This app to increase your productivity.")


for todo in todos:
    st.checkbox(todo)


st.text_input(label="", placeholder="Enter your todo")