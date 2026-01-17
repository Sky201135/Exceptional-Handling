try:
    num1, num2 = eval(input("Enter two numbers separated by a comma: "))
    result = num1/num2print("Result is", result)

except ZeroDivisionError:
    print("Division by zero is error!!")

except SyntaxError:
    print("Comma is missing. enter numbers seperated by a comma.")

except:
    print("wrong input")

else:
    print("no exceptions")

finally:
    print("This will execute no matter what")