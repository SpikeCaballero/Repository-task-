# this is a simple calculation program as seen in class

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
    
    except ZeroDivisionError:
        print("Sorry but you can't divide by Zero! ")

user_name = input("Please enter your name : ").capitalize()
user_number1 = float(input("Please enter the first number of your calculation : "))
user_number2 = float(input("Please enter the second number of your calculation : "))

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

calc = calculation(user_number1, user_number2, operator)
print(f" well, {user_name} your calculation of {user_number1} {operator} {user_number2} = {calc} ")


