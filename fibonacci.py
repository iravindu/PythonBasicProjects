#print("Enter a number?")
import random


fibonacci = []
n = int(input("Enter a number: "))
for i in range(0,n):
   #element = int(input("Enter an element : "))
   if i==0:
      element = 0
      fibonacci.append(element)
   elif i<=2 and i!=0:
      element = 1
      fibonacci.append(element)
   else:
      element = fibonacci[i-1]+fibonacci[i-2]
      fibonacci.append(element)
         
print(fibonacci)   
