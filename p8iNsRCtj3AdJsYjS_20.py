
import string
​
def title_to_number(s):
    ABC = '0' + string.ascii_uppercase
    values = []
    for i,v in enumerate(s[::-1]):
        values.append((ABC.index(v), i))
    return sum(x * 26**v for x,v in values)

