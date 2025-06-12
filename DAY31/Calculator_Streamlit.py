import streamlit as st

st.title("Calculator: ")
num1 = st.number_input("Enter a number:")
num2 = st.number_input("Enter another number:")
col1,col2 = st.columns([1,1])
with col1:
    if st.button("Addition - to find sum of two numbers"):
        st.write(f"Answer is {num1+num2}")
with col2:
    if st.button("Subtraction - to find the difference between two numbers"):
        st.write(f"Answer is {num1 - num2}")
col3,col4 = st.columns([1,1])
with col3:
    if st.button("Multiplication- to find the product of two numbers"):
        st.write(f"Answer is {num1 * num2}")
with col4:
    if st.button("Division"):
        st.write(f"Answer is {num1 / num2}")