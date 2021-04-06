
import re
def score_it(s):
    a = re.findall(r'\d+',s)
    b = [ ]
    for match in re.finditer(r'\d+', s):
        b.append(match.end())
    if not a:
        return 0
    ans = [s[:i].count('(') - s[:i].count(')') for i in b]
    return sum(int(i) * j for i,j in zip(a,ans))

