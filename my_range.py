import random


class MyRange:
    def __init__(self, start, stop, jump):
        self.start = start
        self.current = self.start
        self.stop = stop
        self.jump = jump

    # black-box
    # signature
    def __iter__(self):
        return self

    def __next__(self):
        x = int(input('number'))
        if x % 2 == 0:
            raise StopIteration
        value = self.current
        self.current += self.jump
        return random.randint(1, 100)

it = MyRange(1, 10, 1)
for x in it:
    print(x)

