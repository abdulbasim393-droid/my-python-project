with open("test.txt", "a+") as file:
    content = input("Enter paragraph you want to add :")
    file.write(content)
    file.seek(0)
    data = file.read()
    print(data)
#    data = file.read()
#    print(data)

#    for line in file:
#        print(line)

#    print(file.readline())