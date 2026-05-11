import re

passw = input("Enter your password: ")
check = r"^.{8,}$"
if re.match(check, passw):
    check2 = r"^(?=.*[A-Z])(?=.*[0-9])"

    if re.match(check2, passw):
        print("strong password")
    else:
        print("Weak password")
else:
    print("Enter more than 8 charecters") 