class MyMeta(type):

    counter = 0

    def __init__(cls, name, bases, dic):
        type.__init__(cls, name, bases, dic)
        cls._order = MyMeta.counter
        MyMeta.counter += 1


class MyType(metaclass=MyMeta):    # Python 3
    def __init__(self):
        self.check = True


class My2Type(metaclass=MyMeta):
    class2 = None
    print("Inside My2type")


print(MyType.counter)
print(MyType().check)

