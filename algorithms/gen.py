# # a = int(input('Give amount: '))
#
# def fib(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b
#
# print(list(fib(a)))

def prime(num):
    if num < 0:
        return False
    else:
        if num%2 == 0:
            return False
        else:
            #stop = num/2+1
            for i in range(3,num, 2):
                print(i)
                if num%i == 0 :
                    return False
            return True

print (prime(5))




