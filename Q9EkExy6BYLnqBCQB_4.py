
from collections import deque
​
def wrap_around(string, offset):
    result = deque(list(string))
    result.rotate(-1*offset)
    return ''.join(result)

