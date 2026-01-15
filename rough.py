# lst = [1,2,3]
# my_str = "mlops playlist"
# my_int = 355

# print(type(my_int))
# lst.capitalize()
# my_str = my_str.capitalize()
# print(lst)

from oops_proj import chatbook

# user = chatbook()


## Function vs method 
# lst = [1,2,3]

# Function
# a1 = len(lst)
# print(a1)

# method -- when a function gets defined under a class then it is called method 
# user1 = chatbook()
# user1.sendmsg()

## magic method or dunder methods

## Self Keyword -- Helps in binding objects to the class method 
# use id() to know the memory address of object

## You can define attributes from outside the class

## Encapsulation -- when you dont want all the attributes of a class to get 

## how to encapsulate and how to fetch it from outside
# from oops_proj import chatbook 
# user1 = chatbook()
# print(user1._chatbook__name)


## Getter and Setter -- Methods to get the hidden attribute and set the hidden attribute
# from oops_proj import chatbook 
# user1 = chatbook()
# print(user1.get_name())
# user1.set_name("Agent X")
# print(user1.get_name())


# Understanding the use of static method and variable 
from oops_proj import chatbook
user1 = chatbook()
print(user1.id)

chatbook.set_id(10)

user2 = chatbook()
print(user2.id)

user3 = chatbook()
print(user3.id)