
import re
def longest_substring(digits):
    regex = r'({e}?({o}{e})*{o}?)|({o}?({e}{o})*{e}?)'.format(e='[02468]', o='[13579]')
    return max((x[0] for x in re.findall(regex, digits)), key=len)

