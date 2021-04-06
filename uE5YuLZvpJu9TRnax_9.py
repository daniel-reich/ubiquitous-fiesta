
from collections import deque
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
            return int(token)
def prefix(expr):
    return parse(deque(expr.split()))

