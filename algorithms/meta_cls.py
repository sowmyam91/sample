import pdb


class MyMeta(type):

    counter = 0

    def __init__(cls, name, bases, dic):
        pdb.set_trace()
        type.__init__(cls, name, bases, dic)
        cls._order = MyMeta.counter
        MyMeta.counter += 1


class MyType(metaclass=MyMeta):    # Python 3
    def __init__(self):
        pdb.set_trace()
        self.check = True


class My2Type(metaclass=MyMeta):
    pass


print(MyType.counter)
print(MyType().check)

