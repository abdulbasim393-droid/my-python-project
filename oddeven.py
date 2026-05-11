numbers=list(map(int, input("Enter numbers with space:").split()))
oddoreven = {n: ( "Even" if n%2==0 else "odd") for n in numbers }
print(oddoreven)