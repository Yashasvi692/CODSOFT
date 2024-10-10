def calculate(n1,n2,op):
    if op == "+":
        return n1+n2
    elif op=="-":
        return n1-n2
    elif op=="*":
        return n1*n2
    elif op=="/":
        if n2!=0:
            return n1/n2
        else:
            return "Error"
    elif op=="%":
        if n2!=0:
            return n1%n2
        else:
            return "Error"    
    else:
        return "Enter the correct Operation"
def calc():
    print("CALCULATOR")
    try:
        n1=float(input("Enter First Number: "))
        n2=float(input("Enter Second Number: "))
    except ValueError:
        print("Invalid Input")
        return
    op=input("\nEnter the Operation Symbol (+,-,*,/,%):")
    res=calculate(n1,n2,op)
    print(f"The result of {n1} {op} {n2} is: {res}")
if __name__=="__main__":
    calc()               