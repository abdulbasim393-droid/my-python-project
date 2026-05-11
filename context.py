class Contexting:

#    def __init__(self, filename, method):
#       self.file = open(filename, method)

    def __enter__(self):
        print("starting block")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("end block", exc_type)

with Contexting():
    print("Hello")
    print(10/0)