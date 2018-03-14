from twisted.internet import reactor

def func(value):
    print("INSIDE Func {0}".format(value,))

reactor.callLater(3, func, "FUNC")
print dir(reactor)
reactor.run()
