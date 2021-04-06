
import re
def dakiti(sentence):
    lst = re.findall(r'\d+',sentence)
    s = re.sub(r'\d+','',sentence).split()
    ans = [j for i,j in sorted(zip(lst,s))]
    return ' '.join(ans)

