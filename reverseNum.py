import time
print("Reverse Number Generator")
print("---------------------------")

x = input("Enter the number : ")
y = len(x)
newStr = ""

for i in range(0,y):
    if i==0:
        newStr = x[y-1]
    else:
        newStr = newStr + x[y-i-1]
    
print(f"Reversed Number is : {newStr}")

time.sleep(5)
