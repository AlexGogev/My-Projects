def add(n1, n2, *args):
    res = n1+n2+sum(args)
    print(res)

add(1,2,4,4)


def adding(*args):
    res = 0
    for i in args:
        res += i
    return res

print(adding(1,5,4,3))


#####

def calc(n, **kwargs):
        n += kwargs["add"]
        n *= kwargs["multiply"]

calc(4, multiply=5, add=5)


class Car:
    def __init__(self, **kwargs):
        self.doors = kwargs["doors"]
        self.color = kwargs.get("color")

toyota = Car(doors=4, )
print(toyota.color)