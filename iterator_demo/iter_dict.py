class DictValuesIterator:
    def __init__(self, data):
        self.data = data  # Store the dictionary
        self.keys = list(self.data.keys())  # Get keys in a list
        self.index = 0  # Track position

    def __iter__(self):
        return self  # The iterator itself

    def __next__(self):
        if self.index >= len(self.keys):
            raise StopIteration  # Stop when all keys are used
        key = self.keys[self.index]  # 'a', 'b', 'c', 'd'
        self.index += 1
        return self.data[key]  # Return value of current key

# Example usage:
data_dict = {"a": 10, "b": 20, "c": 30, "d": 40}
iterator = DictValuesIterator(data_dict)

for value in iterator:
    print(value)
