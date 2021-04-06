
import re
def score_it(s):
    nums = re.findall(r'\d+', s)
    s = ' ' + s + ' '
    for n in nums:
        s = re.sub(r'(?<=\D){}(?=\D)'.format(n), '~', s)
    s = s[1:-1]
    num_idx, level, score = 0, 0, 0
    for c in s:
        if c == '(':
            level += 1
        elif c == ')':
            level -= 1
        elif c == '~':
            score += int(nums[num_idx]) * level
            num_idx += 1
    return score

