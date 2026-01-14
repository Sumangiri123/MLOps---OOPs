# intiate a class
class employee :
    # special method/magic method/dunder method -- constructor
    def __init__(self):
        print("Started executing attributes/data")
        self.id = 123
        self.salary = 50000
        self.designation = "Data Science" 
        print("attributes/data have been intiated")
    def travel(self,destination):
        print("This travel function we called manually")
        print(f"employee is now travelling to {self.designation}")


# create a object/instance of the class
sam = employee()

# printing the attributes
# print(sam.id)

# calling a method
# sam.travel("Kerala")

print(type(sam))