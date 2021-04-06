
import re
​
def longest_run(lst):
​
    codes = {1:'A', -1:'D'}  # A: ascending, D: descending
    deltas = ''.join([codes[a - b] if (a - b) in [-1, 1] else '*'
              for a, b in zip(lst[:len(lst)-1], lst[1:])])
​
    runs = [len(element) for element in re.findall(r'A+|D+', deltas)]
​
    return max(runs) + 1 if runs else 1

