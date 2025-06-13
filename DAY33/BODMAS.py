import streamlit as st

st.title("Welcome - BODMAS Expression Evaluator")
st.write("This is BODMAS Evaluator:")
st.write("B - Brackets")
st.write("O - Off")
st.write("D - Division")
st.write("M - Multiplication")
st.write("A - Addition")
st.write("S - Subtraction")

st.write("Sample code")
code = '''
#Here is the sample code to solve a BODMAS expression code in python
#Evaluate function
    def evaluate(expression):
        try:
            result = eval(expression)
            reurn result
        except Exception as e:
            print("error")
            return None       
     exp = input("Enter math expression -(e.g., 2 + 3 * (4 - 1))")
     print(evaluate(exp))
            '''
st.code(code)
expression = st.text_input("Enter a math expression -(e.g., 2 + 3 * (4 - 1))")

if st.button("Evaluate"):
    try:
        result = eval(expression)
        st.success(f"Result: {result}")
    except Exception as e:
        st.error(f"Invalid expression! Error: {e}")
