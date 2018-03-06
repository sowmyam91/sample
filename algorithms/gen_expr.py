import pdb


def odds(arg):
    # Yield odd elements in the iterable.
    for a in arg:
        if a % 2 != 0:
            yield a


items = [100, 101, 102, 103, 104, 105]

# Display all odd items.
# for item in odds(items):
#     print(item)


data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
i = 0

while i < 100:
    double = list(x * 2 for x in data)
    i += 1
    print(double)