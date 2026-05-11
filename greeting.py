name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"My name is {name} and I am {age} years old")



a,b = list(map(int, input("Enter two numbers you want to add: ").split()))

print(f"Sum = {a + b:>10}")