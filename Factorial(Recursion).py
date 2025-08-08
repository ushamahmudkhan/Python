def fact (a):
    if(a == 0):
        return 1
    else:
        return (a * fact(a-1))

num = int(input("Enter number here: "))
result = fact(num)
print("The factorial is : ",result)