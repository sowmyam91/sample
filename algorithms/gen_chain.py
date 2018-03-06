
def integers():
    print("Integers called")
    for i in range(1, 9):
        print("Before Int yield")
        yield i
        print("After Int yield")


def squares(seq):
    print("squares called")
    for i in seq:
        print("before sq yield")
        yield i*i
        print("After sq yield")


def negate(seq):
    print("Negate called")
    for i in seq:
        print("before Neg yield")
        yield -i
        print("After Neg yield")


a = negate(squares(integers()))
print(list(a))


"""
Chained genrators
"""
integers = range(9)
cube = (i * i * i for i in integers)
mod2 = (-i for i in cube if i%2 == 0 )

print (list(mod2))