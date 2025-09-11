# #for loop statement

# for i in range(5):
#      print("HELLO")
    
# print()

# for i in range(10):
#     print("DYPCET")
    
# print()

# for i in range(1,10):
#     print(i,end="")
    
# print()
    
# n=int(input("Enter a number:"))
# for i in range(1,n):
#      print(i,end=" ") 

# print()
        
# for i in range(100,0,-1):
#     print(i,end=" ")
    
# print()

# n=int(input("Enter value of n:"))
# for i in range(n,0,-1):
#     print(i,end=" ")
   
# print()
 
# n=int(input("Enter value of n:"))
# if n>0:
#  for i in range(1,n+1):
#     print(i,end=" ")
# if n<0:
#   for i in range(n,2):
#     print(i,end=" ")

# print()

# for i in range(11):
#     if i%2!=0:
#         print(i,end=" ")

# print()

# for i in range(65,91):
#     print(chr(i),end=" ")

# print()

# sum=0
# for i in range(1,6):
#     sum+=i
# print(sum)

# print()

# n=int(input("Enter n:"))
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print(sum)

# print()

# n=int(input("Enter n:"))
# fact=1
# for i in range(1,6):
#     fact=fact*i
# print(fact)

print()

for i in range(1,11):
    print("2*",i,"=",2*i)

print()

sum=0
for i in range(1,11):
    if i%2==0:
      sum+=i
     
print(sum)

print()

n=int(input("Enter a number:"))
for i in range(1,n+1):
    if i%2==0:
        print(i)

print()

n=int(input("Enter a number:"))
for i in range(n,1,-1):
    if i%2==1:
        print(i)

print()

for i in range(90,64,-1):
    print(chr(i),end=" ")

print()

# # to ask user they want to print capital or small alphabet
user=input("do you want capital or small alphabet?(c/s):")
if user=="c" or user=="C":
    print("Capital alphabet:")
    for i in range(65,91):
        print(chr(i),end=" ")
if user=="s" or user=="S":
    print("Small alphabet:")
    for i in range(97,123):
        print(chr(i),end=" ")
else:
    print("Invalid input")

print( )

for i in range(74,91):
    print(chr(i),end=" ")

print()

#sum of 1 to n odd num 
n=int(input("Enter a num:"))
sum=0
for i in range(1,n+1):
    if i%2==1:
        sum+=i
print(sum)

print()

# print n1 to n2
n1=int(input("Enter a n1:"))
n2=int(input("Enter a n2:"))
for i in range(n1,n2+1):
    print(i)

print( )

# enter n1 and n2(print sum of all even number)
n1=int(input("Enter a n1:"))
n2=int(input("Enter a n2:"))
sum=0
for i in range(n1,n2+1):
    if i%2==0:
        sum+=i
print("Sum of all even no in n1 to n2: "+str(sum))
