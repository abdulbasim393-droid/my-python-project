class Employee:
    def __init__(self, name, age):
        self.name = name       # public
        self.__age = age        # private

    def get_age(self):
        return self.__age



class SubEmployee(Employee):
    def show__age(self):
        print("Age:", self.get_age())   # Accessible in subclass

name=input("Enter your name:")
age=int(input("Enter your age:"))

emp = SubEmployee(name, age)
print(emp.name)        # Public accessible
print(emp.age)
#emp.show__age()         # Private accessed through subclass