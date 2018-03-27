class Fib(object):
    def __init__(self):
        self.prev=0
        self.curr=1

    def __next__(self):
        value = self.curr
        self.curr+=self.prev
        self.prev=value
        yield value

def func(n):
    for i in range(n):
        yield i**2

print(func(5))