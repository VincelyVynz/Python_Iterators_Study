# ---------------------------- Keyword Finder ---------------------------- #

class KeywordFinder:
    def __init__(self, filename, keyword):
        self.filename = filename
        self.keyword = keyword.lower()
        self.keyword_count = 0
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
                self.keyword_count += 1
                return f"{self.keyword_count} - {self.keyword_line}"
            else:
                return self.__next__()
        else:
            print (f"Number of lines with the keyword {self.keyword} = {self.keyword_count}")
            self.contents.close()
            raise StopIteration

    def print_keyword_line(self):
        try:
            print(self.__next__())
            self.print_keyword_line()
        except StopIteration:
            pass



