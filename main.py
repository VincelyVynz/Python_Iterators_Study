# -------------------------- Iterators -------------------------- #

from typing import Iterable, Iterator, Generator

users = ["Bob", "Carol", "David", "John", "Smith"]

# for user in users:
#     print(user)

looper = iter(users)
while True:
    try:
        user = next(looper)
        print(user)
    except StopIteration:
        break




# people : list[str] = ["Mike", "Bob", "Joe", "George"]
#
# people_iter: Iterator[str] = iter(people)
#
# print(next(people_iter))
# print(list(people_iter))
# print(list(people_iter))
# print(list(people_iter))
# print(list(people_iter))

