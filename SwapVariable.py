num1 = int(input("Enter First number here: "))
num2 = int(input("Enter Second number here: "))

temp = num1

print("Before swapping: ", num1, num2)

temp = num1
num1 = num2
num2 = temp

print("After swappping: ", num1, num2)

#without using third variable
print("Before Swapping without third variable: ", num1, num2)

num1, num2 = num2, num1

print("After Swapping without third variable: ",num1, num2)