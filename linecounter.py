# ---------------------------- Line Counter ---------------------------- #

class LineCounter:
    def __init__(self, filename):
        self.filename = filename
        try:
            self.content = open(self.filename, 'r')
        except FileNotFoundError:
            self.content = None
            print(f"Could not find {self.filename}")
        self.line_count = 0
        self.word_count = 0
        self.processed = False

    def process_file(self):
        if self.content is not None:
            line = self.content.readline()
            if line == "":
                self.content.close()
                self.processed = True
                return self.line_count
            else:
                self.line_count += 1
                self.word_count += len(line.split())
                self.process_file()
        return None

    def get_line_count(self):
        if not self.processed:
            self.process_file()
        print(self.line_count)

    def get_word_count(self):
        if not self.processed:
            self.process_file()
        print(self.word_count)
