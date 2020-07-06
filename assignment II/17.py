def calculator(x,y,operator):
    if operator == "+":
        return x+y
    elif operator == "-":
        return x-y
    elif operator == "*":
        return x*y
    elif operator =="%":
        return x%y
    elif operator == "/":
        try:
            return x/y
        except ZeroDivisionError:
            print("Can't divide by Zero....")
        else:
            print("Invalid operator")

answer = 'y'
answer.lower()
while answer.casefold() == 'y':
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operator = input("Enter an operator [+,-,*,%,/]:")
    except ValueError or NameError:
        print("Value error")
        if NameError:
            break
    print(calculator(num1,num2,operator))
    answer = input("Anymore [y/n] ?")
