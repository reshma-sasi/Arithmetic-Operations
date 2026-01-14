# BASIC ARITHMATIC OPERATIONS

num_1=int(input("Enter first number : "))
num_2=int(input("Enter second number : "))

addition=num_1+num_2
substraction=num_1-num_2
multiplication=num_1*num_2
if num_2!=0:
    division=num_1/num_2
else:
    division="Undefined (division by zero)"

print("Addition : ",addition)
print("Substraction : ",substraction)
print("Multiplication : ",multiplication)
print("Division : ",division)
