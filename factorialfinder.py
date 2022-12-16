print("*************FACTORIAL FINDER*************")
print("------------------------------------------")
userPrompt = "Y"

while userPrompt == "Y":
    num = int(input("Please an integer: "))
    print("------------------------------------------")
    factorial = num
    for i in range(1,num):
        factorial = factorial*(num-i)

    print("The Factorial of "+str(num)+" is "+str(factorial) + "!")
    print("------------------------------------------")
    userPrompt = input("Do you want to find the factorial of another number? (Y/N): ")
    print("-----------------------------------------------------")