def add(num1, num2):
    res = num1 + num2
    print((res))
def sub(num1, num2):
    res = num1 - num2
    print((res))
def mul(num1, num2):
    res = num1 * num2
    print((res))
def div(num1, num2):
    try:
        res = num1 / num2
        print((res))
    except Exception as e:
        print("Exception raised:",e)

def calculator():
    try:
        print("Please select operation -\n 1. Add \n 2. Subtract \n 3. Multiply \n 4. Divide\n") 
        select = int(input("Select operations form 1, 2, 3, 4 :")) 
  
        x = int(input("Enter first number: ")) 
        y = int(input("Enter second number: ")) 
        
        if select == 1: 
            add(x, y)
        elif select == 2: 
            sub(x, y)
        elif select == 3: 
            mul(x, y)
        elif select == 4: 
            div(x, y) 
        else: 
            print("Invalid input") 
            calculator()
    except Exception as e:
        print("You can't put anything but integer numbers")
    finally:
        calculator()
calculator()