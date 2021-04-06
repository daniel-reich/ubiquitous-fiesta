
import re
def switcheroo(txt):
    return ' '.join([x.replace('nce','nts') if re.search(r'nce[!?.,]*$',x) else x.replace('nts','nce') if re.search(r'nts[!?.,]*$',x) else x for x in txt.split()])

