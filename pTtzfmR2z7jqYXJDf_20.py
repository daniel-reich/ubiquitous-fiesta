
from collections import Counter
def possible_palindrome(txt):
    counter = Counter(txt)
    values = counter.values()
    total_letters = sum(values)
    odd_total = sum(i for i in values if i%2 != 0)
    even_total = sum(i for i in values if i%2 == 0)
    if (odd_total%2 != 0 and total_letters - odd_total >= 2)\
    or (total_letters in (odd_total,even_total) \
    and total_letters > len(counter.keys())):
        return True
    else:
        return False

