# from operators import add
# from operators import subtract
# from operators import divide
# from operators import multiply
# x = add(12 , 34)
# y = subtract(45 , 89)

# print(x,y)
import operators
import others
import trig

operator = input("Please input operator: ")
if operator == "cube":
    num = eval(input("Enter number: "))
    x = others.cube(num)
    print(x)
elif operator == "sin":
    angle = eval(input("Enter angle in degrees: "))  
    sin_of_angle = trig.get_sine(angle)   
    print(sin_of_angle)

elif operator == "cos":
    angle = eval(input("Enter angle in degrees: ")) 
    print(trig.get_cos(angle))

elif operator == "tan":
    angle = eval(input("Enter angle in degrees: "))
    print(trig.get_tan(angle))

else:   
    num1 = eval(input("Input number1 :"))
    num2 = eval(input("Input number2 :"))
   

    if operator == "+":
      x = operators.add(num1,num2)
      print(x)
    elif operator == "-":
      x = operators.subtract(num1,num2)
      print(x)
    elif operator == "*" or "x" or "X":
      x = operators.multiply(num1,num2) 
      print(x)
    elif operator == "/":
      x = operators.divide(num1,num2) 
      print(x)      
