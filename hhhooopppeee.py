class PowerOfTwoIterator:
    def __init__(self, max_power):
        self.max_power = max_power
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.max_power:
            raise StopIteration
        result = 2 ** self.current
        self.current += 1
        return result

if __name__ == "__main__":
    power_iterator = PowerOfTwoIterator(10)

    for value in power_iterator:
        print(value)
