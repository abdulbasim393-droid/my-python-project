word=input("Enter your string:")
vowels="aeiouAEIOU"
result="".join([char for char in word if char not in vowels])
print("String without viwels:", result)