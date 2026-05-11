import re

email = input("Enter your e-mail:")
check = r"^[\w\.-]+@[\w\.-]+\.\w+$"
if re.match(check,email):
    print("Valid email")
else:
    print("Invalid email")
