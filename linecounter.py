# ---------------------------- Line Counter ---------------------------- #

class LineCounter:
    """
    This module defines the LineCounter class, which reads a text file
    and counts the number of lines and words in it.

    Args:
        filename (str): Path to the text file you want to analyze.

    Usage:
        counter = LineCounter("example.txt")
        counter.get_line_count()  # Prints number of lines
        counter.get_word_count()  # Prints number of words
    """
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

        """
               Processes the file, reading it line by line.

               Counts the number of lines and words in the file.
               Uses recursion to read through the entire file.

               Returns:
                   int or None: Total number of lines if completed, or None while processing.

       """

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
        """
               Prints the number of lines in the file.

               If the file hasn't been processed yet, this will trigger processing.

        """

        if not self.processed:
            self.process_file()
        print(self.line_count)

    def get_word_count(self):

        """
                  Prints the number of words in the file.

                  If the file hasn't been processed yet, this will trigger processing.

       """
        if not self.processed:
            self.process_file()
        print(self.word_count)
