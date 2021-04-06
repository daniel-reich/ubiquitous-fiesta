
import re
def numbers_need_friends_too(n):
    grouped = [g.group(0) for g in re.finditer(r'(\w)\1*', str(n))]
    result = ""
    for item in grouped:
        result += item * 3 if len(item) == 1 else item
    return int(result)

