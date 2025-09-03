class Counter:
    """
    Custom iterator that counts from 1 up to a given value.

    Args:
        count (int): The maximum number to count up to.

    """

    def __init__(self, count):
        """
        Initializes the counter.
        """
        self.count = count
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.count:  # Checks if the current value is less than the given count value to continue counting
            self.current += 1
            return self.current

        else:
            raise StopIteration

    def print_number(self):
        """
        Prints the number one by one till the limit is reached
        """
        try:
            print(self.__next__())
            self.print_number()
        except StopIteration:      # Stops iteration when the limit is reached
            pass
