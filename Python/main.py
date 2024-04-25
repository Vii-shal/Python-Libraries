# # import cv2
# # import math

# # this is a comment

# # print ("hello world")
# # print (math.gcd(3,6))
# # print(5+5)

# # if (age<18):
# #     print("hello")

# # a=34
# # b="vishal"
# # print(type(a))
# # print(type(b))

# #  typecasting
# # a = float(a)
# # print(type(a))
# # print(a)

# # string
# name="harry"
# hlo="       good morning       "
# house="Wel Come"
# # name='harry'
# # name='''harry 
# # good morning'''
# print(name)
# print(name[0])
# print(name[2:4])
# print(hlo.strip())
# print(len(name))
# var=house.lower()
# print(var)
# var=house.upper()
# print(var)
# var=house.replace("e","Z")
# print(var)

# stu = "vishal, veer, imu"
# var=stu.replace(",",'\n')
# print(var)

# stri = "This is a "
# name = "harry"
# stri2 = "This is not a"
# print(stri + name)

# name1="shiv"
# name2="ravi"
# temp = "this is a {} and he is a good  boy named {}".format(name1,name2)
# print(temp)
# temp = "this is a {1} and he is a good  boy named {0}".format(name1,name2)
# print(temp)
# temp = f"this is a {name1} and he is a good boy {name2}"
# print(temp)

# # operators
# print(2**3)
# print(10//3)
# print(10%3)




'''
Python Collections
1. List
2. Tuple
3. Set
4. Dictionary
'''

# list 
'''
list = [61,2,3,4,6,41]
var = type(list)
print(var)
print(list)

list[2]=22222
print(list) 

var = list[2:4]
print(var)

var = list.pop()
print(var)

list.insert(1,10000000)
print(list)

list.append(555)
print(list)

del list
print(list)

'''


# tuple

'''
a=("hlo","how","are","you")
# a[0]="good"                    #not possible
'''

# set 

'''
a={11,1,28,99,3,99,99,1,9,9,3,1,12}
print(a)

a.add(5555555555)
print(a)

a.update([5,6,7,8,5,1,1,7,2])
print(a)

a.remove(7)
print(a)

a.descard(58464)
print(a)

# like list we can also use : .pop   .clear   del
# and ...   intersection  union
'''

# dictionary 

'''
vishDict = {
    "Name" : "Vishal" ,
    "Class" : "10th" ,
    "Marks" : 34.55 ,
    "Hours In School" : 6 
}
print(vishDict)

print(vishDict["Marks"])

vishDict["Marks"] = 100
print(vishDict)

vishDict.pop("Marks")
print(vishDict)
'''

# conditional 

'''
a=int(input("enter n \n"))
if(a<18):
    print("cant vote")
elif(a==18):
    print("you are a teen")
else:
    print("you can vote")

'''

# loop

'''
for i in range(1,10):
    print(i)
    i=i+1

li=[1,23,"this",88]
for item in li:
    print(item)


dic={"name":"gill","class":"ist"}
for d in dic:
    print(d)

'''

# function

'''
def greet():
    print("good morning")
greet()

def sum(a,b):
    c=a+b
    return c

d = sum(34,6)
print(d)
'''


# oop 

'''
class Employee:
    def __init__(self,gname,gsalary):         #constructor
        self.name = gname
        self.salary = gsalary
    def getsalary(self):
        return self.salary

vishal = Employee("veer",100)
print(vishal.name)
print(vishal.salary)
s = vishal.getsalary()
print (s)
'''




# file I/O 

'''
# wriring a file ---------------------------------------------------------- 

s="i am a lovely person"

# with open("me.txt","w") as m:
#     m.write(s)

fp = open("text.txt","w")
fp.write(s)
fp.close()
'''

'''
# reading a file ----------------------------------------------------------

with open("vishal.txt","r") as r:
    s=r.read()
print(s)
'''