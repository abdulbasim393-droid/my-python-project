class Print:
    def __init__(self,max):
        self.num = 1
        self.max = max

    def __iter__(self):
        return self
  
    def __next__(self):
        if self.num <= self.max:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration
number=int(input("Enter how many number you want to print:"))
counter = Print(number)
for i in counter:
    print(i, end=" ")



