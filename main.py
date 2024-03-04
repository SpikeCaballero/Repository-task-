# this is a simple calculation program as seen in class
# calculation function collecting two variables and a mathematical operator
def calculation(number1, number2, mathematical_operator):

    try:

        if mathematical_operator == '+':
            result = number1 + number2
            return result
        
        elif mathematical_operator == '-':
            result = number1 - number2
            return result
        
        elif mathematical_operator == 'x':
            result = number1 * number2
            return result
        
        elif mathematical_operator == '/':
            result = number1 / number2
            return result
    # try except clause to prevent crashing for user trying to divide by zero
    except ZeroDivisionError:
        print("Sorry but you can't divide by Zero! ")
# data collection, Name and numbers
user_name = input("Please enter your name : ").capitalize()
user_number1 = float(input("Please enter the first number of your calculation : "))
user_number2 = float(input("Please enter the second number of your calculation : "))
# operator list to ensure correct input
ops = ['+', '-', 'x', '/']
while True:

    operator = input("""Please enter the mathematical operator to perform on your numbers : 
                 For example : +, -, x, / 
                 :  
                 """)
    if operator not in ops:
        print("That's not one of the options, please try again! ")
        continue
    else:
        print("Calculating......")
        break
# calling of calculation function and printing of the result.
calc = calculation(user_number1, user_number2, operator)
print(f" well, {user_name} your calculation of {user_number1} {operator} {user_number2} = {calc} ")


