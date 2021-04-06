
import re, string
def findShortestWords(txt):
    shortest = 10000
    shortest_lst = []
    lst = re.compile(r"(?:^|(?<=\s))[A-Za-z0-9_'\-]+(?=\s|$|\b)").findall(txt.lower())
    for word in lst:
        if len(word) < shortest and all(char in string.ascii_letters for char in word):
            shortest = len(word)
    for word in lst:
        if len(word) == shortest and all(char in string.ascii_letters for char in word):
            shortest_lst.append(word)
    return sorted(shortest_lst)

