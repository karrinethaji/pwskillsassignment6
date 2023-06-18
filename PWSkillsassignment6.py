#!/usr/bin/env python
# coding: utf-8

# ### PW Skills Assignment 6 on OOPS

# #### Q1, Create a vehicle class with an init method having instance variables as name_of_vehicle, max_speed and average_of_vehicle.

# In[1]:


class vehicle:
    def __init__(self,name_of_vehicle,max_speed,average_of_vehicle):
        self.name_of_vehicle=name_of_vehicle
        self.max_speed=max_speed
        self.average_of_vehicle=average_of_vehicle
obj_vehicle=vehicle("Car",120,100)


# #### Q2. Create a child class car from the vehicle class created in Que 1, which will inherit the vehicle class.Create a method named seating_capacity which takes capacity as an argument and returns the name of the vehicle and its seating capacity.

# In[2]:


class vehicle:
    def __init__(self,name_of_vehicle,max_speed,average_of_vehicle):
        self.name_of_vehicle=name_of_vehicle
        self.max_speed=max_speed
        self.average_of_vehicle=average_of_vehicle
    
class child_vehicle(vehicle):
    
    def seating_capacity(self,capacity):
        self.capacity=capacity
        return f"The name of the vehicle is:{self.name_of_vehicle}, The seating capacity of the vehicle: {self.capacity}"
    
obj_child_vehicle=child_vehicle("suzuki",990,800)
obj_child_vehicle.seating_capacity(1000)


# #### Q3. What is multiple inheritance? Write a python code to demonstrate multiple inheritance.

# Multiple inheritance --> When a class can be derived from more than one base class this type of inheritance is called multiple inheritances. In multiple inheritances, all the features of the base classes are inherited into the derived class/child class.

# In[3]:


class Mother:
    mothername = ""
 
    def mother(self):
        print(self.mothername)
 
# Base class2
 
 
class Father:
    fathername = ""
 
    def father(self):
        print(self.fathername)
 
# Derived class
 
 
class Son(Mother, Father):
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)
 
 
# Driver's code
s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents()
s1.father()
s1.mother()


# #### Q4. What are getter and setter in python? Create a class and create a getter and a setter method in this class.

# Getter, setter is used to get or set the value of the private attribute. Let's create a class and getter and setter methods to access the private attribute below:

# In[4]:


class Vehicle:
    def __init__(self,a,b):
        self.a=a
        self.__b=b # b is the private variable
    def get_b(self): #getter method
        return self.__b
    def set_b(self,new_b): # setter method
        self.__b=new_b
obj_veh=Vehicle(10,20) # object declaration
print("Before setting the new value to private attribute :",obj_veh.get_b()) # accesing the value of private attribute using the getter method
obj_veh.set_b(200) # setting the new value for the private attribute using set_b method
print("After setting new value to private attribute :",obj_veh.get_b())


# #### Q5.What is method overriding in python? Write a python code to demonstrate method overriding.

# Method overriding is an ability of any object-oriented programming language that allows a subclass or child class to provide a specific implementation of a method that is already provided by one of its super-classes or parent classes. When a method in a subclass has the same name, same parameters or signature and same return type(or sub-type) as a method in its super-class, then the method in the subclass is said to override the method in the super-class.

# In[5]:


class Vehicle():
      
    # Constructor
    def __init__(self):
        self.value = "Inside Parent"
          
    # Parent's show method
    def show(self):
        print(self.value)
          
# Defining child class
class Suzuki(Vehicle):
      
    # Constructor
    def __init__(self):
        self.value = "Inside Child"
          
    # Child's show method
    def show(self):
        print(self.value)
          
          
# Driver's code
obj1 = Vehicle()
obj2 = Suzuki()
  
obj1.show()
obj2.show() # Parent class also have show method but child class overridden that method as the child class alrady have a same method

