
import re
def bracket_logic(old):
    new = re.sub('[^\[\](){}<>]+', '', old)
    while new != old:
        old, new = new, re.sub(r'\(\)|\[\]|<>|{}', '', new);
    return new == ''

