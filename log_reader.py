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
        self.content = open(self.filename, 'r')
        self.line_count = 0
        self.word_count = 0
        self.processed = False

    def process_file(self):
        line = self.content.readline().strip()
        if line == "":
            self.content.close()
            self.processed = True
            return self.line_count
        else:
            self.line_count += 1
            self.word_count += len(line.split())
            self.process_file()

    def get_line_count(self):
        if not self.processed:
            self.process_file()
        print(self.line_count)

    def get_word_count(self):
        if not self.processed:
            self.process_file()
        print(self.word_count)

