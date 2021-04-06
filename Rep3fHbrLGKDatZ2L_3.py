
import re
def complete_pattern(s):
    for c in sorted(set(s) - {'_'}, reverse=True):
        new_s = re.sub('_', c, s)
        pattern = r'(.*[{}].*)(\1)(.*)'.format(c)
        lst = re.findall(pattern, new_s)
        if lst:
            tpl = lst[0]
            if len(tpl) == 3 and new_s == ''.join(tpl):
                len3 = min(len(tpl[0]), len(tpl[2]))
                if tpl[0][:len3] == tpl[2][:len3]:
                    return c
    return -1

