#Get words longer than 4 letters from list

lists=input("Enter your list elements with space:").split()
letters = [word for word in lists if len(word) > 4]
print (letters)