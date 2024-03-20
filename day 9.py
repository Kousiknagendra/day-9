# 1.) Write a Python script to generate and print a dictionary that 
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2.)Find the uncommon words from 2 strings

# # s1 = "Hello how are you"
# s2 = "Hello how is"

# 3.)Wrire a code print the 8th fibanochi number



# 2.)Find the uncommon words from 2 strings

# s1 = "Hello how are you"
# s2 = "Hello how is"




'''
s1 = "Hello how are you"
s2 = "Hello how is"

s1 = s1.split(" ")
s2 = s2.split(" ")
for val in s1:
    if val not in s2:
        print(val)
for val in s2:
    if val not in s1:
        print(val)

are
you
is
'''

# 3.)Wrire a code print the 8th fibanochi number
'''
num = 8
n1=0
n2=1

for val in range(num):
    ans = n1+n2
    n1 = n2
    n2= ans
print(ans)

34
'''

# constructors
#Eg:2
# unparameteraised condtructor
'''
class profile:
    def  __init__(self):
        print("hello world")

obj = profile()
obj.__init__()

hello world
hello world
'''

#Eg:3
# parameteraised
'''
class profile:
    def __init__(self, id, name, age):
        print(id,name,age)

obj = profile(1, "Kousik", 20)

1 Kousik 20
'''

#Eg:4
'''
class c1:
    name="Kousik"
    place="Bagnlore"
    
    def m1(self):
        print(self.name, self.place)

object = c1()
object.m1()

Kousik Bagnlore
'''
'''
class c1:
    email = "kousik@gmail.com"
    
    def m1(self):
        name="Kousik"
        place="Bagnlore"
        print(name,place)
        print(self.email)

object = c1()
object.m1()

Kousik Bagnlore
kousik@gmail.com
'''

#Eg:5
''''
class c1:
    def m1(self):
        name="Kousik"
        age= 20
        return name, age
    def display(self):
       # print(name,age)
       # print(self.name, self.age)
        print(self.m1())
    

object = c1()
object.display()

('Kousik', 20)
'''

# Eg:6
# to use the variable inside the constructor in another methods
'''
class class1:
    def __init__(self):
        self.name = "Kousik"
        self.email = "Kousik@gmail.com"
        #return name, email # error ---> cannot use return with constructor

    def display(self):
        print(self.name, self.email)

c1 = class1()
c1.display()

Kousik Kousik@gmail.com
'''


# ! -------------> Inheritance
# The process of utilising methods and attributes of parent class
# throughuot the object of chilod class it is called inheritence

# ? 5 types of inheritence
# Single inheritence
# Mutilevel inheritence
# Multiple inheritence
# Hybrid inheritence
# Heirarichal inheritence


# Single inheritence
# it has only one parent class and only child class

#Eg:1
'''
class parent:
    def m1():
        print("I am parent class")

parent.m1()

class child:
    def m2(self):
        print("I am child class")

I am parent class
'''

''''
class parent:
    def m1(self):
        print("I am parent class")

class child(parent):
    def m2(self):
        print("I am child class")

obj = child()
obj.m1()

I am parent class
'''

#Eg:2
'''
class c1:
    def __init__(self):
        print(" I am consturctor from parent class")

class child1(c1):
    pass

obj = child1()

I am consturctor from parent class
'''

# Eg:3
'''
class parent:
    name = "Kousik"


class child(parent):
    name = "name1"
    def display(self):
        print(self.name)

d = child()
d.display()
'''

# Mutilevel inheritence
#Eg:1
'''
class voice:
    def sound(self):
        print("All thse animals have their own voice")

class dog(voice):
    def dog_voice(self):
        print("bark")

class cat(dog):
    def cat_voice(self):
        print("meow")
        
class parrot(cat):
    def parrot_voice(self):
        print("speack")

        
all = parrot()
all.dog_voice()
all.cat_voice()
all.sound()
all.parrot_voice()
        
bark
meow
All thse animals have their own voice
speack
'''

#Eg:2

'''
class honda_city:
    def engine_specs(self, cc, hp, torque, fuel_type, num_of_piston):
        print(self, cc, hp, torque, fuel_type, num_of_piston)

        def body_specs(self,  color, weight, height, lenght, vehicle_type):
            print(color, weight, height, lenght, vehicle_type)

class amaze:
        def amaze_engine_specs(self, cc, hp, torque, fuel_type, num_of_piston):
            print(self, cc, hp, torque, fuel_type, num_of_piston)

        def amaze_body_specs(self,  color, weight, height, lenght, vehicle_type):
            print(color, weight, height, lenght, vehicle_type)

class civic(amaze):
        def civic_engine_specs(self, cc, hp, torque, fuel_type, num_of_piston):
            print(self, cc, hp, torque, fuel_type, num_of_piston)

        def civic_body_specs(self,  color, weight, height, lenght, vehicle_type):
            print(color, weight, height, lenght, vehicle_type)

class honda:
    pass

honda= honda()
honda.honda_city_engine_specs(1500, 230, 2979, "petrol", 4)
honda.civic_body_specs("white", 2000, 5.5, 8, "Hatchback")
'''

#3.) Multiple Inheritence
# -> It has multiple parent and 1 child
'''
class while_petrol:
    def function1(self):
        print("used to Airplans")

class organic_petrol:
    def function_o(self):
        print("used for bike, cars")

class premium_petrol:
    def function_p(self):
        print("sports car, bikes")

class petrol(while_petrol, organic_petrol, premium_petrol):
    def defanition(self):
        print("petrols type")

p=petrol()
p.defanition()
p.function_o()


petrols type
used for bike, cars
'''

# Eg:2
# MRO ----->  method resolution order
'''
class addition:
    def add(self,a,b):
        print(a+b)

class subtract:
    def sub(self,a,b):
        print(a-b)

class multiply:
    def mul(self,a,b):
        print(a*b)

class divison(addition, subtract,multiply):
    def div(self,a,b):
        print(a/b)

calc = divison()
calc.add(3, 4)
calc.mul(5, 2)

7
10
'''
'''
class addition:
    def add(self,a,b):
        print(a+b)
    def mul (self,a,b):
        print(a%b)

class subtract:
    def sub(self,a,b):
        print(a-b)

class multiply:
    def mul(self,a,b):
        print(a*b)

class divison(addition, subtract,multiply):
    def div(self,a,b):
        print(a/b)

calc = divison()
calc.add(3, 4)
calc.mul(5, 2)

7
1
'''
# ! Heirarical inheritance
'''
class catagory:
    def weight(self,weight):
        print(weight)

class Tomato(catagory):
    def tomato_specs(self):
        color ="black"
        taste ="neutral taste"

class carrot(catagory):
    def carrot_specs(self):
        color ="green"
        taste ="sweet"

c = carrot()
c.carrot_specs()
c.weight("30gms")

30gms
'''
'''
class catagory:
    def weight(self,weight):
        print(weight)

    def display(self,color,taste):
        print(color,taste)

class Tomato(catagory):
    def tomato_specs(self):
        color ="black"
        taste ="neutral taste"
        self.display(color, taste)

class carrot(catagory):
    def carrot_specs(self):
        color ="green"
        taste ="sweet"

c = carrot()
c.carrot_specs()
c.weight("30gms")

t = Tomato()
t.tomato_specs()
t.weight("20gms")

30gms
black neutral taste
20gms
'''

# Hybrid inheritence
# The combimation of above 4 inheritance is called Hybrid inheritence


'''
class c1:
    def m1(self):
        print("class1")

class c2(c1):
    def m2(self):
        print("class2")

class c3(c2):
    def m3(self):
        print("class3")

class c4(c3):
    def m4(self):
        print("class4")

    def m3(self):
        print(" i am m3 from c4")

class c5(c4):
    def m5(self):
        print("class5")
        
class c6(c5, c3):
    def m6(self):
        print("class6")

obj = c6()
obj.m3()

 i am m3 from c4

'''

# --------------------------:> polymorphism
# poly - many,  morph - form
# A function which has the ability more than 1 functionally
# then it is considered to be as polymorphism

# polymorphism in built in functions
#len() ----> which is used to find the length of list, tuple,dict etc....
#index()
#max()
#min()
#count()
#pop()
# and more...,


# * polymorphism in operators

# +
'''
print(8+8)
print("k" + '1')
print([1,2,3]+[5,6])


16
k1
[1, 2, 3, 5, 6]
'''

# *

'''
print(6*7)
l1 = {1,2,3,4,5,6}
print(*l1)
#def f1(*args)
l1 = [1,2,3,4]
print(11*20)

42
1 2 3 4 5 6
220
'''

# polymorphism in classes
# We can achieve polymorphism in 2 ways
# 1.) Method overloading
# 2.) Method overriding

#) Tasks


#Write the code for the belwo tasks using function
#1.) d1 = {"shirt": 1000, "pant"; 1500, "Shoes"; "900", "handkey": 30}
#a.) Find the min ans max priced product
#b.) Find the product starts with 's' and 'S'

#2.) Find then 67, is strong number or not

#3.) 11 = [1,2,3,4,5,6]
#n=2--> [5, 6, 1,2,3,4]
#n=3--> [4,5,6, 1,2,3]


