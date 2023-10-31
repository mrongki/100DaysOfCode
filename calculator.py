import os, sys

#Calculator
logo = '''
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \\     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \\_|  | || |    / /\\ \\    | || |    | |       | || |  / .'   \\_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \\   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \\ `.___.'\\  | || | _/ /    \\ \\_ | || |   _| |__/ |  | || |  \\ `.___.'\\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
'''
#Add
def add(n1, n2):
    return n1 + n2


#Subtract
def subtract(n1, n2):
    return n1 - n2


#Multiply
def multiply(n1, n2):
    return n1 * n2


#Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}
def calculator():
    print(logo)
    num1 = float(input('What\'s the first number?: '))
    for key in operations:
        print(key)
        
    isDoneCalc = False
    while not isDoneCalc:
        op = input('Pick an operation: ')
        while op not in operations:
            print('Error: Operation not found...')
            op = input('Pick an operation: ')
        function = operations[op]
        num2 = float(input('What\'s the next number?: '))
        ans = function(num1, num2)
        print(f'{num1} {op} {num2} = {ans}')
            
        user_input = input(f'Type "y" to continue calculating with {ans}, or type "n" to start a new calculation.: ')
        if user_input in ['y', 'yes']:
            num1 = ans
        elif user_input in ['n', 'no']:
            isDoneCalc = True
            os.system('cls')
            calculator()
        else:
            sys.exit()

calculator()