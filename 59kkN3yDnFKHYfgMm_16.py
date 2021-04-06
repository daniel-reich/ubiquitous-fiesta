
import re
def best_friend(txt, a, b):
    return a not in re.sub(a+b,'',txt) and a!=b

