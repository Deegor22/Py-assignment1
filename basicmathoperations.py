num1=input("Enter the first number: ")
num2=input("Enter the second number: ")
a=float(num1)
b=float(num2)

print()
print("Addition: ",a+b)
print("Subtraction: ",a-b)
print("Multiplication: ",a*b)
if b != 0:
  print("Division: ",a/b)
else:
  print("Division: cannot be divided by 0")
