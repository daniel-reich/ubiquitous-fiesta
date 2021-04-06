
from collections import deque
​
def parse(tokens):
    token=tokens.popleft()
    if token=='+':
            return parse(tokens)+parse(tokens)
    elif token=='-':
            return parse(tokens)-parse(tokens)
    elif token=='*':
            return parse(tokens)*parse(tokens)
    elif token=='/':
            return parse(tokens)/parse(tokens)
    else:
            # must be just a number
            return int(token)
​
def prefix(exp):
    return parse(deque(exp.split()))

