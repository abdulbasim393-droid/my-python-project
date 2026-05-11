class Duck:
    def sound(self):
        return "Quack"
class Person:
    def sound(self):
        return "I'm Quacking like a duck!"
def make_sound(obj):
    print(obj.sound())
a=input("Do u want Duck sound or Person making Quack:").lower()
if a == "duck":
    make_sound(Duck())
elif a == "person":
    make_sound(Person())
else:
     print("wrong input")
#make_sound(Duck())
#make_sound(Person())