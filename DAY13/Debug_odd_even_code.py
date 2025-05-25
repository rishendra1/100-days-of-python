'''
Question: debug the code:-
def odd_or_even(number):
    if number % 2 = 0:
        return "This is an even number."
    else:
        return "This is an odd number."
    Output: Error
Error details

cannot assign to expression here. Maybe you meant '==' instead of '='? (exercise.py, line 2)
'''
#Debugged version of code
def odd_or_even(number):
    if number % 2 == 0:
        return "This is an even number."
    else:
        return "This is an odd number."