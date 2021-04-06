
import re
def markdown(symb):
    def inner(st, wrd):
        return re.sub('(?i)'+wrd+'[\.,!?]*', lambda m: symb+m.group(0)+symb, st)
    return inner

