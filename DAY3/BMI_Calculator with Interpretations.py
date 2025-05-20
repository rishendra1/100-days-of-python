#BMI Calculator with Interpretations

Height = float(input("What is your height (in m)?"))
Mass = float(input("What is your weight (in kg)?"))
BMI = Mass / (Height**2)
print(f"Your BMI is {BMI}")
if BMI >= 0 and BMI <= 18.5:
    print("underweight")
elif BMI > 18.5 and BMI <= 25:
    print("overweight")
elif BMI > 25:
    print("overweight")
else:
    print("Invalid BMI")