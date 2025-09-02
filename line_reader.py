

class LineReader:
    def __init__(self, filename):
        self.filename = filename
        try:
            self.contents = open(self.filename, 'r')
        except FileNotFoundError:
            print(f"Could not find {self.filename}")

    def __iter__(self):
        return self

    def __next__(self):
        line = self.contents.readline()

        if line:
            return line
        else:
            self.contents.close()
            raise StopIteration