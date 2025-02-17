import random

class MyRange:
    def __init__(self, start, stop, jump):
        self.start = start
        self.current = self.start
        self.stop = stop
        self.jump = jump

    def first(self):
        self.current = self.start

    # black-box
    # signature
    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.stop:
            raise StopIteration
        value = self.current
        self.current += self.jump
        return value

it = MyRange(1, 10, 1)
for x in it:
    print(x)

# build iterator
# return factorial
# mf = MyFactorial(1, 5)
# for x in mf:
#    print(x)
# 1!
# 2!
# 3!
# 4!
# 5!

