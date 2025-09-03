from counter import Counter
from keyword_finder import KeywordFinder
from linecounter import LineCounter

# story = KeywordFinder('textfile.txt', keyword="[ERROR]")
#
# story.print_keyword_line()


lc = LineCounter("textfile.txt")

lc.get_line_count()
lc.get_word_count()