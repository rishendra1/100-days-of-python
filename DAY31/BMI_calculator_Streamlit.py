import streamlit as st

st.title("BMI Calculator")
st.subheader("Calculates the BMI value of a person")
st.caption("Sample code is given below")
def bmi_calculator(w,h):
    return w/(h*h)
code_sample = '''
    def BMI_Calculator(weight,height):
        return weight / (height**2)
    w = int(input("Enter weight: "))
    h = int(input("Enter height: "))
    Result = BMI_Calculator(w,h)
    print(result)
'''
st.code(code_sample)
st.subheader("Calculate your BMI here: ")
weight = st.number_input("Enter Weight: ",min_value=1.0,step=0.1)
height = st.number_input("Enter Height: ",min_value=0.1,step=0.01)
if st.button("Calculate BMI"):
    result = bmi_calculator(weight,height)
    st.write(f"Your BMI is {result}")