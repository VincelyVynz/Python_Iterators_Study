# TODO 1 Find and print lines containing they keyword
# TODO 2 Count the number of times the keyword is repeated.
# TODO 3 Count total number of lines and words

class KeywordFinder:
    def __init__(self, filename, keyword):
        self.filename = filename
        self.keyword = keyword.lower()
        self.keyword_line = None
        try:
            self.contents = open(self.filename, 'r')
        except FileNotFoundError:
            print(f"Could not find {self.filename}")

    def __iter__(self):
        return self

    def __next__(self):
        line = self.contents.readline()
        if line:
            if self.keyword in line.lower():
                self.keyword_line = line
                return self.keyword_line
            else:
                return self.__next__()
        else:
            self.contents.close()
            raise StopIteration

    def print_keyword_line(self):
        try:
            print(self.__next__())
            self.print_keyword_line()
        except StopIteration:
            pass


# ---------------------------- Line Counter ---------------------------- #

class LineCounter:
    def __init__(self, filename):
        self.filename = filename
        self.line_count = 0
        try:
            self.contents = open(self.filename, 'r')
        except FileNotFoundError:
            print(f"Error! Could not find {self.filename}")

    def __iter__(self):
        return self

    def __next__(self):
        line = self.contents.readline()
        if line:
            self.line_count += 1
            return self.line_count
        else:
            self.contents.close()
            self.total_lines = self.line_count
            self.get_line_count()
            return self.total_lines

    def get_line_count(self):
        if self.contents.closed:
            print(self.total_lines)
        else:
            self.__next__()
