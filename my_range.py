
class Iterable:

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
        if self.current >= self.stop:
            raise StopIteration
        value = self.current
        self.current += self.jump
        return value


