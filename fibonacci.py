#print("Enter a number?")
import random
#number = input("Pls enter a number: ")
#print(number)

#randNum = random.randint(0,100)
#print(randNum)
#length = 10
#myList = []
#print(len(myList))
#newList = myList
#ewList = myList+1
#for i in myList:
   # newList[i] = myList[i]+1
   # print(newList)
#count = 10
#for i in count:
#    print (i)
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
