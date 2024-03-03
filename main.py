# this is a simple calculation program as seen in class

def calculation(number1, number2, mathematical_operator):

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
    

user_number1 = float(input("Please enter the first number of your calculation : "))
user_number2 = float(input("Please enter the second number of your calculation : "))

operator = input("""Please enter the mathematical operator to perform on your numbers : 
                 For example : +, -, x, / 
                 :  
                 """)

calc = calculation(user_number1, user_number2, operator)
print(calc)
