from counter import Counter
from keyword_finder import KeywordFinder
from linecounter import LineCounter

story = KeywordFinder('textfile.txt', keyword="[ERROR]")

story.print_keyword_line()

print("\n"* 3)

lc = LineCounter("textfile.txt")

lc.get_line_count()
lc.get_word_count()

print("\n"* 3)

counter = Counter(5)
counter.print_number()
