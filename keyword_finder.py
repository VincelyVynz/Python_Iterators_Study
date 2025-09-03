# ---------------------------- Keyword Finder ---------------------------- #

class KeywordFinder:
    """
    This module defines the KeywordFinder class, which reads a text file and
    finds all lines that contain a given keyword (case-insensitive).

    Args:
        filename (str): Path to the text file to search.
        keyword (str): The keyword to look for in each line (case-insensitive).

    Example:
        finder = KeywordFinder("example.txt", "error")
        finder.print_keyword_line()  # Prints all lines with the keyword

        # Or use it like an iterator:
        for line in finder:
            print(line)
    """

    def __init__(self, filename, keyword):
        """
               Initializes the KeywordFinder with a filename and keyword.
               Tries to open the file for reading.
        """

        self.filename = filename
        self.keyword = keyword.lower()
        self.keyword_count = 0
        self.keyword_line = None
        try:
            self.contents = open(self.filename, 'r')
        except FileNotFoundError:
            print(f"Could not find {self.filename}")

    def __iter__(self):
        """
        Returns itself
        """
        return self

    def __next__(self):
        """
              Reads the next line from the file that contains the keyword.
              Prints the total number of lines with the keyword when all lines are read.

              Returns:
                  str: A formatted string with the match number and the matching line.

              Raises:
                  StopIteration: When the end of the file is reached.
        """
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

        """
                Recursively prints each line in the file that contains the keyword.
                Stops when all matches have been printed.
        """
        try:
            print(self.__next__())
            self.print_keyword_line()
        except StopIteration:
            pass



