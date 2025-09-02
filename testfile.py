from line_reader import LineReader
from log_reader import KeywordFinder

story = KeywordFinder('textfile.txt', keyword="error")

story.print_keyword_line()


