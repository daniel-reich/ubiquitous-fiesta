
from collections import deque
​
​
def shift_letters(txt, n):
    li = deque([a for a in txt if a != ' '])
    listOfSpaces = get_index(list(txt))
    li.rotate(n)
    li = list(li)
    for a in listOfSpaces:
        li.insert(a, ' ')
    return ''.join(li)
​
​
def get_index(lst):
    res = []
    position = 0
    while True:
        try:
            position = lst.index(' ', position)
            res.append(position)
            position += 1
        except ValueError:
            break
    return res

