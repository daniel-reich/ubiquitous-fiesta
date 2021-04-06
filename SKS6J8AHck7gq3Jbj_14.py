
import re
​
def tidy_books(lst):
    regex = re.compile(r'(?P<title>\b.+)(?: - )(?P<author>.*?)(?:\s*$)')
    finalbooks = []
    for book in lst:
        newbook = [regex.search(book[0]).group('title'), regex.search(book[0]).group('author')]
        finalbooks.append(newbook)
    return finalbooks

