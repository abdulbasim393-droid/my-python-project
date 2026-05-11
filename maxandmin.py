arr = list(map(int, input("Enter numbers:" ).split()))
max_val = arr[0]
min_val = arr[0]

for num in arr:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num

print("Max:", max_val, ",", "Min:", min_val)

