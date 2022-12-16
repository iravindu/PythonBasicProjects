import random

# initializing an empty list to store the fibonacci series
fibonacci = []

n = int(input("Enter a number: "))

for i in range(0,n):
   if i==0:
      element = 0
      fibonacci.append(element)
   elif i<=2 and i!=0:
      element = 1
      fibonacci.append(element)
   else:
      element = fibonacci[i-1]+fibonacci[i-2]
      fibonacci.append(element)
         
print("The corresponding fibonacci series")  
print(fibonacci)   
print("-----------------------------------")