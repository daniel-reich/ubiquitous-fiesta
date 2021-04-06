
import re
def switcheroo(txt):
    replacement = {'nts':'nce','nce':'nts'}
    ans = re.sub(r'n[cets]+\b',lambda x:replacement[x.group(0)],txt)
    return ans

