try:
    n=int(input("Enter your mark:"))
    t=int(input("Enter total marks:"))
    percentage=(n/t)*100
except ZeroDivisionError:
    print("Total marks should not be zero")
    percentage = None

except ValueError:
    print("Enter a number:")
    percentage = None
finally:
    if percentage is not None:
        print("Your result is:", percentage)
    else:
        print("Cannot be calculated")