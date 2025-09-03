# 🔁 Python Iterators Study

This repository contains small but practical examples of Python iterators. The purpose of these examples is to understand how iteration works *without using `for` or `while` loops* — focusing instead on `iter()`, `next()`, and implementing the iterator protocol using `__iter__` and `__next__` methods.

---

## 📁 File Overview

| File Name          | Description                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------------------|
| `main.py`          | A simple test file for manually working with `iter()` and `next()` on built-in iterables like lists.|
| `counter.py`       | Defines a custom `Counter` iterator that counts from 1 up to a given number.                        |
| `keyword_finder.py`| Defines `KeywordFinder`, which reads a file and yields lines containing a specified keyword.        |
| `linecounter.py`   | Defines `LineCounter`, which recursively counts total lines and words in a file.                    |
| `testfile.py`      | A scratchpad file for testing all iterator classes.                                                 |
| `textfile.txt`     | A sample file used to test file-reading iterators. *(Not included in the repo.)*                   |

---

## 🔧 Iterators Included

### `Counter` — Custom Number Generator
- **File:** `counter.py`
- **Description:** Yields numbers from 1 to `count`, one by one, using the iterator protocol.

---

### `KeywordFinder` — Filter Lines by Keyword
- **File:** `keyword_finder.py`
- **Description:** Reads a text file and yields only lines containing a specified keyword (case-insensitive). Tracks the number of matching lines.

---

### `LineCounter` — Count Lines and Words in File
- **File:** `linecounter.py`
- **Description:** Recursively reads a file to count total lines and total words. Avoids use of loops by calling itself.

---

## 🚀 How to Run

Run the `testfile.py` script to test all iterator classes together:
Or run each file individually to explore how the iterators work in isolation.
