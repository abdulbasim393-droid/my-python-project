arr = list(map(int, input("Enter the numbers of array:").split()))

arr[0], arr[-1] = arr[-1], arr[0]
print("Array after swapping:", arr)