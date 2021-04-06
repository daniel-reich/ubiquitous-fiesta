
import re
​
def score_it(s):
    groups = re.findall('\(|\)|\d+', s)
    level, score = 0, 0
    for i in groups:
        if i == '(':
            level += 1
        elif i == ')':
            level -= 1
        else:
            score += int(i)*level
    return score

