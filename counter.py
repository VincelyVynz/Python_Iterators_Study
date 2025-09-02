class Counter():
    def __init__(self, count):
        self.count = count
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.count:
            self.current += 1
            return self.current

        else:
            raise StopIteration



