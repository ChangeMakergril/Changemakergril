#myself
print("HEllo Guys")
print("I am Pranali Sagar Nalawade.")
print("I currently study in FYBtech CSE in DYPCET,Kolhapur.")
print("i completed 10th and 12th in Gadhinglaj with good percentage.")
a=16
b=11 
c=2006 
print("My Birth Date",a,"/",b,"/",c)

#operations
a=12
b=13
sum=a+b
diff=a-b
print("The sum of",a,"and",b,"is",sum)
print("The difference of",a,"and",b,"is",diff)


name ="Pranali"
age =19
standard ="FYBTech"
price = 15.5

print("My name is",name,"and age is",age)
print("I learn in",standard)
print(price)

#datatype
print(type(name))
print(type(age))
print(type(price))


#expression execution
Txt="#"
print(3*Txt*2)   #(repeat) String & Numeric with operate * multiply

A="5"
B=2
Txt="^"
print((A+Txt)*B)     #(concatenation)string & string can operate with +


a,b=2,3
c=5
print(a+b*c)        #with arithmetic operators

a,b=10,0.5
print(a*b)         #aruthmetic with float, reuslt in float

a,b=10,50
print(a/b)        #result of division with 2 integers will be float

A=3
B=1.5
print(B/A)
C=B//A         #division with float & int will give int display as float
print(C)

a,b=15,4
c=a//b 
print(c)

a,b=-15,4
c=a//b 
print(c) 

a,b=15,-4 
c=a//b 
print(c)   #floor gives closest integer,which is lesser than or equal to float value 

a,b=-6,4
c=a%b 
print(c) 

a,b=6,4
c=a%b 
print(c) 

a,b=6,-4
c=a%b 
print(c) 

a,b=-6,-4
c=a%b 
print(c)   #remainder is -ve when denominator is negative 

#input() from the user
name=input("Your name:")
age=int(input("Age:"))
price=float(input("Price:"))  

print("Name :",name)
print("Age :",age)
print("Price:",price)

