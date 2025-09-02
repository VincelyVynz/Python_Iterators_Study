from counter import Counter
from log_reader import KeywordFinder, LineCounter

# story = KeywordFinder('textfile.txt', keyword="error")
#
# story.print_keyword_line()


lc = LineCounter("textfile.txt")

lc.get_line_count()