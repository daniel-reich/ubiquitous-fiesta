
import re
def numbers_need_friends_too(n):
    ans = re.findall(r'(.)\1{1,}',str(n))
    return  int(''.join([i*3 if i not in ans else i for i in list(str(n))]))

