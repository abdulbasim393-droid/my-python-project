print("1.Addition")
print("2.Substract")
print("3.Division")
print("4.Multiplication")
print("5.Modulus")
calc = int(input("Enter your choice: "))
if calc >= 1 and calc <= 5:
 
    a,b = list(map(int, input("Enter two numbers: ").split()))

    if calc == 1:
       print(a+b)
    elif calc == 2:
        print(a-b)
    elif calc == 3:
        print(a/b)
    elif calc == 4:
        print(a*b)
    else:
        print(a%b)
else:
    print("Wrong choice")

