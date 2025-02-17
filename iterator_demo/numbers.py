
class Numbers:
    def __init__(self):
        self.midgamim = [1, 4, 6, 8]
        self.partipipents = (2, 99, -3, 50)
        self.rates = (3, 88, 0, 15, 71)

        #                       0                  1           2
        self.all = [self.midgamim, self.partipipents, self.rates]
        self.current_list_index = 0
        self.current_index = 0

    # signature
    def __iter__(self):
        return self

    def __next__(self):
        if self.current_list_index >= len(self.all):
            self.current_list_index = 0
            self.current_index = 0
            raise StopIteration

        current_list = self.all[self.current_list_index]
        value = current_list[self.current_index]
        self.current_index += 1
        if self.current_index >= len(current_list):
            self.current_index = 0
            self.current_list_index += 1
        return value

nums = Numbers()
for number in nums:
    print(number)

