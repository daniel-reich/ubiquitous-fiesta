
from itertools import count
​
def news_at_ten(txt, n):
    pad = ' ' * n
    txt = pad + txt + pad
​
    result = [txt[0:n]]
​
    counter = count(1)
    while True:
        start = next(counter)
        end = start + n
        result.append(txt[start:end])
        if result[-1] == ' ' * n:
            break
​
    return result

