arr = list(map(int, input("Enter array elements: ").split()))
if arr == arr[::-1]:
   print("Palindrome")
else:
   print("Not Palindrome")