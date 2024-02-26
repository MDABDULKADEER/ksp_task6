#datatypes
number1=9  #integer
number2=5.6  #float
name="abdul,kadeer" #set
name1=[1,2,3]  #list
name2=(1,2,3)  #tuple
name3=True     #bool

#type convertion
print(float(number1))  #convert from int to float
print(list(name))      #convert from set to list

#type
sample=str(number1)
print(type(sample))    #type casting

#strings
name0="helloworld"
print(name0[5:])

#operators
#arithmatic op + - * / % **

abdul=1
kadeer=3
print(abdul+kadeer)
print(abdul-kadeer)
print(abdul*kadeer)
print(abdul/kadeer)
print(abdul%kadeer)
print(abdul**kadeer)

#assignment operators: =,+=,-=,*=,/=,**=,%=
abdul1=2
abdul1+= 1
print(abdul1)
abdul1%= 1
print(abdul1)
abdul1-= 1
print(abdul1)
abdul1*= 1
print(abdul1)
abdul1/= 1
print(abdul1)
abdul1**= 1
print(abdul1)

#comparision operators ==,!=,<,>,<=,>=


#if elif else
hello=12
world=15
if hello==world:
    print("hi")
elif hello<world:
    print("kk")
elif hello>world:
    print("ll")
elif hello!=world:
    print("mm")
elif hello<=world:
    print("nn")
elif hello>=world:
    print("oo")
else:
    print("good")

#logical operators: and or not

if hello==world and hello>world:
    print("hi")
elif hello==world or hello>world:
    print("ok")
else:
    print(not(hello==world))

#identity :is isnot
kal=49
lak=49
alk=35
print(kal is lak)
print(lak is not alk)

#membership: in not in
kadeer1="hello guys"
print("hello" in kadeer1)
print("guys" not in kadeer1)

#loops
#for loops
N=int(input())   #input from user
for i in range(N):
    print(N)

#while loops
K=int(input())
j=0
while(j<K):
    print(K)
    j+=1
    