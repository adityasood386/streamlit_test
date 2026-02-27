import streamlit as st
def hey():
    st.write("hello")
st.button("click",help="click here",on_click=hey(),type="primary")


st.title("# Welcome",text_alignment="center")
st.header("My First Page")
st.subheader("My title")
st.markdown("## Welldone")
st.badge("New")
st.badge("Success", icon="🥺", color="green")

name=st.text_input("Enter your name")
password=st.text_input("enter your password",type="password")
rollno=st.text_input("Enter your rollno")
address=st.text_area("Address")
if st.button("submit"):
    st.write("username=",name, " \nRollno=",rollno," \nPassword",password," \nAddress",address)

if st.button("click me"):
    st.snow()