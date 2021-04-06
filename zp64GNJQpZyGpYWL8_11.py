
def score_it(s):
    s = ''.join([c for c in s if c in "()0123456789"])
    s = s.replace('(', ' ( ').replace(')', ' ) ').split()
    depth = 0
    score = 0
    for el in s:
        if el == '(':
            depth += 1
        elif el == ')':
            depth -= 1
        else:
            score += depth * int(el)
    return score

