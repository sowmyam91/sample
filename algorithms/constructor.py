class A:
    def __new__(cls):
        print("A.__new__ called")

    def __init__(self):
        print("INIT")
        self.name = "abc"

    def print_str(self, string):
        print(string)

a = A()
a.print_str("abc")
