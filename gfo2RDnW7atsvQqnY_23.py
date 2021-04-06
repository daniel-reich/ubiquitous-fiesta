
import re
regex = re.compile(r'(:|;)(-|~)?(\)|D)')
def count_smileys(seq):
    cnt = 0
    for i in seq:
        if bool(re.fullmatch(regex,i)):
            cnt += 1
    return cnt

