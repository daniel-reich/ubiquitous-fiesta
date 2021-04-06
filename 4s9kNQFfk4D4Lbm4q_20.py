
import string
upper = list(string.ascii_uppercase)
def ABA(s):
    if s == 'A':
        return 'A'
    if s == 'B':
        return 'ABA'
    else:
        edge = ABA(upper[upper.index(s)-1])
        return edge + s + edge

